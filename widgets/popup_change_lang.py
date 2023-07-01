#!/usr/bin/python3

# Native Python imports
import tkinter as tk

# Project-specific imports
from widgets import Popup
from organizer_grid import OrganizerGrid
from CONSTANTS import *


class PopupChangeLang(Popup):
    """ Creates radio buttons which allow to change program language settings """

    def __init__(
            self,
            root        = None,
            action      = None,
            organizer   = OrganizerGrid(),
    ):
        # Setting the parent class
        super().__init__(root=root, title=LONG_TEXT['changeLang'])
        super().geometry('280x150')  # Window size for the content to appear correctly
        if action is not None:
            super().add_action_button(text=CHANGE, command=lambda: action(self.data_provide()))
        super().add_cancel_button()
        master = self.contentFrame

        list_radiobuttons = {
            'eng': ENGLISH,
            'pl': POLISH,
            'sp': SPANISH,
        }

        self.var = tk.StringVar(value='Option1')

        for element in list_radiobuttons:
            widget = tk.Radiobutton(master,
                                    text=list_radiobuttons[element],
                                    value=element,
                                    variable = self.var,
                                    tristatevalue=0)
            organizer.to_grid(root=master, target=widget, sticky='W')

    def data_receive(self, new_data):
        """ Loads current settings into the Popup """

        raise NotImplementedError("Sending data to the popup change lang is not ready")

    def data_provide(self):
        """ Changes settings  according to selected option """
        
        raise NotImplementedError("The popup change lang is not ready for changing the options")


def main():
    """If the module is called as __main__, a test run of the popup will be performed."""

    root = tk.Tk()
    root.title('Test - Main Window')
    root.geometry('300x400')

    PopupChangeLang(root=root, action=lambda x:print(*x, sep='\n'))

    root.mainloop()


if __name__ == '__main__':
    main()
