#!/usr/bin/python3

# Native Python imports
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# Project-specific imports
from widgets import (ConstructorMenuBar, FrameNavigation, FrameOutput,
                     PopupAdd, PopupDelete, PopupConfirmDelete, PopupUpdate, PopupChangeLang, PopupAbout)
import controller_database as db
from CONSTANTS import *
import window_welcome


class WindowMain(tk.Tk):
    """ Creates Main Window of Database Reader program """

    def __init__(
            self,
            database_file        = None,
            title                = LONG_TEXT['programTitle'],
            controller_db        = db.Database,
            widget_menu_bar      = ConstructorMenuBar,
            widget_nav           = FrameNavigation,
            widget_output        = FrameOutput,
            popup_add            = PopupAdd,
            popup_update         = PopupUpdate,
            popup_delete         = PopupDelete,
            popup_conf_delete    = PopupConfirmDelete,
            popup_chg_lang       = PopupChangeLang,
            popup_about          = PopupAbout,
    ):
        super().__init__()
        super().title(title)

        # Creating database object with database_file
        self.controller_db = controller_db(database_file)

        # Preparing popups
        self.popup_add           = popup_add
        self.popup_update        = popup_update
        self.popup_delete        = popup_delete
        self.popup_conf_delete   = popup_conf_delete
        self.popup_about         = popup_about
        self.popup_chg_lang      = popup_chg_lang

        # Used to store which row is currently displayed in Output
        # and pass this information to Popup
        self.current_row = None

        # Creating Menu Bar

        # --- Creating list of tabs for Menu Bar
        edit_tab = {
            'add': {'nameOption': ADD, 'command': self.call_popup_add},
            'sep1': {'nameOption': SEPARATOR, },
            'update': {'nameOption': UPDATE, 'command': self.call_popup_update},
            'sep2': {'nameOption': SEPARATOR, },
            'delete': {'nameOption': DELETE, 'command': self.call_popup_delete},
        }

        file_tab = {
            'change': {'nameOption': LONG_TEXT['change'], 'command': self.change},
            'sep1': {'nameOption': SEPARATOR, },
            'exit': {'nameOption': EXIT, 'command': self.destroy},
        }

        set_tab = {
            'lang': {'nameOption': LONG_TEXT['changeLang'], 'command': self.call_popup_change_lang},
        }

        help_tab = {
            'about': {'nameOption': LONG_TEXT['about'], 'command': self.call_popup_about},
        }

        menu_tabs_list = {
            'file': {'nameTab': FILE, 'listOptions': file_tab, },
            'edit': {'nameTab': EDIT, 'listOptions': edit_tab, },
            'settings': {'nameTab': SETTINGS, 'listOptions': set_tab, },
            'help': {'nameTab': HELP, 'listOptions': help_tab, },
        }

        # --- Creating Menu Bar with list of tabs
        widget_menu_bar(self, menu_tabs_list)

        # Creating Frames

        # --- Creating Main Frame
        main_frame = ttk.LabelFrame(self, padding=5)
        main_frame.pack(fill='both', expand=True, padx=5, pady=5)

        # --- Creating Paned Window which will allow to control Navigation and Output proportions in width
        paned_window = tk.PanedWindow(main_frame)
        paned_window.pack(fill='both', expand=True,)

        # --- Creating Navigation and filling it with data for the first time
        # --- Assigning the "update_all" method to the Navigation
        nav_frame = tk.Frame(paned_window)
        data_nav = self.controller_db.select_names()
        self.navigation = widget_nav(root=nav_frame, action_nav=self.update_all)
        self.navigation.data_receive(data_nav)
        paned_window.add(nav_frame)

        # --- Creating Output
        output_frame = tk.Frame(paned_window)
        self.output = widget_output(root=output_frame)
        paned_window.add(output_frame)

    def change(self):
        """ Allows to change the database by destroying current window and calling Window Welcome """

        self.destroy()
        window_welcome.WindowWelcome().mainloop()

    def call_popup_add(self):
        """ Creates Popup Add and bind to it a self.add method """

        self.popup_add(root=self, action=self.add)

    def add(self, provided_data):
        """ Adds data to the database """

        # The Popup returns a generator
        # Below code changes it into dictionary
        new_data = dict()
        for data in provided_data:
            new_data[data[0]] = data[1]

        # Preparing data for database.add function
        name = new_data['name']
        problem = new_data['problem']
        solution = new_data['solution']

        # Try to add data, display error popup if data set already exists
        try:
            self.controller_db.add(name, problem, solution)
        except db.sqlite3.IntegrityError:
            showerror(title=ERROR_TEXT['dataSetNameTitle'], message=ERROR_TEXT['dataSetNameMessage'])

        # Update Navigation so the new data set displays on the list
        self.update_nav()

    def call_popup_update(self):
        """ Creates Popup Update and bind to it a self.update method """

        # I create popup window in variable because
        # I will have to reference to it when filling the entry fields
        popup = self.popup_update(root=self, action=self.__update, )

        # Filling the entry fields with current data of currently selected row
        db_data = self.controller_db.select_content(self.current_row)
        for new_data in db_data:  # Unpacking data received from SQLite query
            popup.data_receive(new_data)

    def __update(self, provided_data):
        """ Updates data in currently selected row """

        # The Popup returns a generator
        # Below code changes it into dictionary
        new_data = dict()
        for data in provided_data:
            new_data[data[0]] = data[1]

        # Preparing data for database.add function
        name = new_data['name']
        problem = new_data['problem']
        solution = new_data['solution']

        # Update data
        self.controller_db.update(problem, solution, name)

        # Update Navigation so the new data set displays on the list
        self.update_all(self.current_row)

    def call_popup_delete(self):
        """Creates Popup Delete and binds it to a self.call_popup_conf_delete method"""

        # I create popup window in variable because
        # I will have to reference to it when filling the entry fields
        popup = self.popup_delete(root=self, action=self.call_popup_conf_delete)

        # Filling the entry fields with current data of currently selected row
        db_data = self.controller_db.select_content(self.current_row)
        for new_data in db_data:  # Unpacking data received from SQLite query
            popup.data_receive(new_data)

    def call_popup_conf_delete(self):
        """Creates Popup Confirm Delete and binds it to a self.delete method"""

        # I create popup window in variable because
        # I will have to reference to it when filling the entry fields
        popup = self.popup_conf_delete(root=self, action=self.delete)

        # Filling the entry fields with current data of currently selected row
        db_data = self.controller_db.select_content(self.current_row)
        for new_data in db_data:  # Unpacking data received from SQLite query
            popup.data_receive(new_data)

    def delete(self, provided_data):
        """ Deletes currently selected row """
        # The Popup returns a generator
        # Below code changes it into dictionary
        target = dict()
        for data in provided_data:
            target[data[0]] = data[1]

        """" Deletes currently selected row"""
        self.controller_db.delete(target['name'])

        # Update Navigation so the new data set displays on the list
        self.update_all(self.current_row)

    def call_popup_change_lang(self):
        """ Creates Popup Change Language """

        self.popup_chg_lang(root=self)

    def call_popup_about(self):
        """ Creates Popup About Program """

        self.popup_about(root=self)

    def update_nav(self):
        """ Updates Navigation basing on a query to database """

        newData = self.controller_db.select_names()
        self.navigation.data_receive(newData)

    def update_output(self, target):
        """ Updates Output basing on provided data """

        db_data = self.controller_db.select_content(target)
        for new_data in db_data:  # Unpacking data received from SQLite query
            self.output.data_receive(new_data=new_data)

    def update_all(self, target):
        """ Updates Output basing on provided data
            Updates Navigation basing on query to database """

        self.current_row = target
        self.update_output(target)
        self.update_nav()


def main():
    """If the module is called as __main__, a test run of the window will be performed."""

    root = WindowMain(database_file='Test database.db')
    root.mainloop()


if __name__ == '__main__':
    main()
