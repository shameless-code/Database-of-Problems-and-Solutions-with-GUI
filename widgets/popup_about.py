#!/usr/bin/python3

# Native Python imports
import tkinter as tk

# Project-specific imports
from widgets import Popup
from CONSTANTS import *


class PopupAbout(Popup):
    """ Creates popup with basic info about program """

    def __init__(
            self,
            root    = None,
    ):
        # Setting the parent class
        super().__init__(root=root, title=LONG_TEXT['about'])
        super().add_cancel_button()
        self.mainFrame.configure(text=HI)  # Adds text to the frame, a pretty little detail
        master = self.contentFrame

        # Putting content in the Popup Window
        self.content = tk.Label(master, text=ABOUT_PROGRAM)
        self.content.pack()


def main():
    """If the module is called as __main__, a test run of the popup will be performed."""

    root = tk.Tk()
    root.title('Test - Main Window')
    root.geometry('300x400')

    PopupAbout(root=root)

    root.mainloop()


if __name__ == '__main__':
    main()
