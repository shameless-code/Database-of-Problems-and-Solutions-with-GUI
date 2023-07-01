#!/usr/bin/python3

# Native Python imports
import tkinter as tk

# Project-specific imports
from widgets import InOutTextField
from organizer_grid import OrganizerGrid
from CONSTANTS import *


class FrameOutput:
    """ Creates Outputs fields that display data """

    def __init__(
            self,
            root=None,
            organizer=OrganizerGrid(),
    ):
        list_widgets = {
            'name':NAME,
            'problem':PROBLEM,
            'solution':SOLUTION,
        }
        # dynamic_elements is a dictionary "name:widget" of is_modifiable widgets
        # only elements listed in it can be updated via "data_receive" method
        self.dynamic_elements = dict()

        for element in list_widgets:
            if element == 'name':
                # Name field does not have a description label
                # Because I think presented data that looks better that way
                widget = InOutTextField(root, height=1, width=100, is_modifiable=False)
                organizer.to_grid(root=root, target=widget)

                self.dynamic_elements[element] = widget
            else:
                widget = tk.Label(root, text=list_widgets[element])
                organizer.to_grid(root=root, target=widget, sticky='w', scalable=False)
                widget = InOutTextField(root, height=12, width=100, is_modifiable=False)
                organizer.to_grid(root=root, target=widget)

                self.dynamic_elements[element] = widget

    def data_receive(self, new_data):
        """ Updates Output fields basing on provided dictionary,
            the dictionary must have keys matching names of fields """

        for element in self.dynamic_elements.items():
            if element[0] in new_data.keys():
                element[1].update_field(new_data[element[0]])
            else:
                # Each field without matching key in the dictionary
                # Will display "No data" info
                element[1].update_field(LONG_TEXT['noData'])


def main():
    """If the module is called as __main__, a test run of the frame will be performed."""

    root = tk.Tk()
    root.geometry('300x400')

    FrameOutput(root=root)

    root.mainloop()


if __name__ == '__main__':
    main()
