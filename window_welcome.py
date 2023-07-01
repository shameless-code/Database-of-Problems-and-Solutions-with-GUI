#!/usr/bin/python3

# Native Python imports
import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showerror

# Project-specific imports
import controller_database as db
from CONSTANTS import *
import window_main


class WindowWelcome(tk.Tk):
    """ Window Welcome allows to create and launch in Targeted Window
        a new Database or to select an existing one """

    def __init__(
            self,
            title               = LONG_TEXT['select'],
            controller_db  = db.Database,
    ):
        super().__init__()
        super().title(title)
        self.controller_db = controller_db

        # "Create" section    #
        label_create = ttk.LabelFrame(self, text=LONG_TEXT['create'], padding=5)
        create_var = tk.StringVar()
        entry_create = tk.Entry(label_create, width=50, textvariable=create_var)
        button_create = tk.Button(label_create, text=CREATE, command=lambda: self.create_check(create_var.get()))

        entry_create.grid(row=0, column=0)
        button_create.grid(row=0, column=1)
        label_create.pack(side=tk.TOP, fill='both', expand=True, padx=5, pady=5)

        # "Select" section    #
        label_select = ttk.LabelFrame(self, text=LONG_TEXT['select'], padding=5)
        entry_var = tk.StringVar()
        entry_select = tk.Entry(label_select, width=50, textvariable=entry_var)
        button_select = tk.Button(label_select, text=FIND, command=lambda: entry_var.set(self.load_database()))
        button_ok = tk.Button(label_select, text=SELECT, command=lambda: self.exist_check(entry_var.get()))

        entry_select.grid(row=0, column=0)
        button_select.grid(row=0, column=1)
        button_ok.grid(row=1, column=0, columnspan=2)
        label_select.pack(side=tk.BOTTOM, fill='both', expand=True, padx=5, pady=5)

    def create_database(self, databaseName):
        """ Creates a new database and in it creates basic table for Database Reader """

        new_db = self.controller_db(databaseName)
        new_db.create_table()

    @staticmethod
    def load_database():
        """ Creates a dialog window that allows to select a database file """

        try:
            file = askopenfile(
                mode='r',
                title=LONG_TEXT['select'],
                filetypes=[(LONG_TEXT['dbFiles'], '*.db'), (LONG_TEXT['allFiles'], '*.*')]
            )
            if file is not None:
                return file.name
            else:
                return ''  # Without the return of empty string StringVar() updates itself to None
        except tk.TclError:
            # An error that occurs if Root window is closed when askopenfile is still open
            return 0

    def create_check(self, databaseName):
        """ Basic checks before creating a new database """

        if databaseName == '':  # User did not provided a name for database
            showerror(title=ERROR_TEXT['noNameTitle'], message=ERROR_TEXT['noNameMessage'])
        elif os.path.isfile(databaseName):  # Provided name already exists
            showerror(title=ERROR_TEXT['existTitle'], message=ERROR_TEXT['existMessage'])
        else:
            self.create_database(databaseName)
            self.start_targeted_window(databaseName)

    def exist_check(self, file):
        """ After providing the path with file name there is a check if file exists,
            if there is no errors Targeted Window starts """

        if os.path.isfile(file):
            self.start_targeted_window(file)
        else:
            try:
                showerror(title=ERROR_TEXT['notFoundTitle'], message=ERROR_TEXT['notFoundMessage'])
            except tk.TclError:
                # An error that occurs if Root window is closed when showerror is still open
                # No functionality problems, so I just silenced it
                return 0

    def start_targeted_window(self, file):
        """ After a check of the database table and rows, starts the Targeted Window """

        try:  # Check if database has required table with required rows
            database = db.Database(file)
            database.check_file()
        except db.sqlite3.DatabaseError:  # Error if something is wrong with database
            showerror(title=ERROR_TEXT['validTitle'], message=ERROR_TEXT['validMessage'])
        else:
            self.destroy()  # Window Welcome destroy itself
            window_main.WindowMain(file).mainloop()  # Targeted Window became initialized


def main():
    """ Starts the Window Welcome """

    root = WindowWelcome()
    root.mainloop()


if __name__ == '__main__':
    main()
