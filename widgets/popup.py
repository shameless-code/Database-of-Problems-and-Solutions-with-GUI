#!/usr/bin/python3

# Native Python imports
import tkinter as tk
from tkinter import ttk

# Project-specific imports
from CONSTANTS import *


class Popup(tk.Toplevel):
    """ Creates the Popup window, can take 2 arguments:
        - "root" to point a parent widget
        - "title" for the Popup window's title """

    def __init__(
            self,
            root            = None,
            title           = None,
    ):
        # Creating Popup Window
        super().__init__(root)
        super().title(title)

        # Creating Main Frame (frame for all other frames)
        self.mainFrame = ttk.LabelFrame(self, padding=5)
        self.mainFrame.pack(side='top', fill='both', expand=True, padx=5, pady=5)

        # Creating Frame for content
        self.contentFrame = tk.Frame(self.mainFrame)
        self.contentFrame.pack(side='top', fill='both', expand=False, )

        # Creating Frame for bottom buttons
        self.bottomButtons = tk.Frame(self.mainFrame)
        self.bottomButtons.pack(side='bottom', fill='both', expand=False, )

    def add_action_button(self, text=None, command=None):
        """ Adds the Action button with provided text and command """

        buttonAction = tk.Button(self.bottomButtons, text=text, command=command)
        buttonAction.pack(side='right')

    def add_cancel_button(self):
        """ Adds the Cancel button which closes the Popup """

        buttonCancel = tk.Button(self.bottomButtons, text=CANCEL, command=self.destroy)
        buttonCancel.pack(side='right')


def main():
    """If the module is called as __main__, a test run of the popup will be performed."""

    root = tk.Tk()
    root.title('Test - Main Window')
    root.geometry('300x400')

    Popup(root=root, title='popup 1').add_cancel_button()

    popup2 = Popup(root=root, title='PopUp 2')
    popup2.add_cancel_button()
    popup2.add_cancel_button()
    popup2.add_cancel_button()

    popup3_text = 'ACTION TIME\n(I will print "Action start!" in the terminal)'
    popup3 = Popup(root=root, title='POPUP 3')
    popup3.add_action_button(text=popup3_text, command=lambda: print('Action start!'))
    popup3.add_cancel_button()

    root.mainloop()


if __name__ == '__main__':
    main()
