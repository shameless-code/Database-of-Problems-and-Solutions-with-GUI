#!/usr/bin/python3

# Native Python imports
import tkinter as tk
from tkinter.ttk import Treeview

# Project-specific imports
from CONSTANTS import *


class FrameNavigation:
    """Creates Navigation which can be filled with data from a list
     and the return position selected from the list."""

    def __init__(
            self,
            root=None,
            action_nav=None,
    ):

        self.action_nav = action_nav
        self.navigation = Treeview(root)
        self.navigation.heading('#0', text=NAVIGATION)
        self.navigation.pack(fill='both', expand=True, side=tk.LEFT)
        scrollbar = tk.Scrollbar(root)
        scrollbar.config(orient="vertical", command=self.navigation.yview)
        scrollbar.pack(fill='y', expand=False, side=tk.RIGHT)

        self.navigation.bind('<Double-1>', lambda event: self.choose_position())
        # lambda takes 'event' argument because .bind always returns it, but I want to ignore it

    def data_receive(self, new_data):
        """Updates Navigation with provided list."""

        self.navigation.delete(*self.navigation.get_children())
        for content in new_data:
            self.navigation.insert('', tk.END, text=content)

    def choose_position(self):
        """Returns the selected position on Navigation."""

        try:
            nav_item = self.navigation.selection()[0]
            name_item = self.navigation.item(nav_item, 'text')
            self.action_nav(name_item)
        except IndexError:
            pass
            # Some little bug when clicking on one position of a Treeview to many times
            # No functionality problems, so I just silenced it


def main():
    """If the module is called as __main__, a test run of the frame will be performed."""

    root = tk.Tk()
    root.geometry('300x300')

    FrameNavigation(root=root)

    root.mainloop()


if __name__ == '__main__':
    main()
