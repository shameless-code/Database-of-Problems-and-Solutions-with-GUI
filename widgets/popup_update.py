#!/usr/bin/python3

# Native Python imports
import tkinter as tk

# Project-specific imports
from widgets import Popup
from widgets import InOutTextField
from organizer_grid import OrganizerGrid
from CONSTANTS import *


class PopupUpdate(Popup):
    """ Creates entry fields which allow for updating a row of data. """

    def __init__(
            self,
            root        = None,
            action      = None,
            organizer   = OrganizerGrid(),
    ):
        # Setting the parent class
        super().__init__(root=root, title=LONG_TEXT['update'])
        if action is not None:
            super().add_action_button(text=UPDATE, command=lambda: action(self.data_provide()))
        super().add_cancel_button()
        master = self.contentFrame

        # List of widgets present in the frame
        list_widgets = {
            'name': NAME,
            'problem': PROBLEM,
            'solution': SOLUTION,
        }

        # data_elements is a dictionary "name:widget" of data-providing widgets
        # only elements listed in it returns values via "data_provide" method
        self.data_elements = dict()

        # Creating widgets, placing and registering them in data_elements
        for element in list_widgets:
            if element == 'name':
                # 'name' entry is only 1 row high
                widget = InOutTextField(master, height=1, width=100, is_modifiable=False)
                organizer.to_grid(root=master, target=widget)

                self.data_elements[element] = widget
            else:
                widget = tk.Label(master, text=list_widgets[element])
                organizer.to_grid(root=master, target=widget, sticky='w', scalable=False)
                widget = InOutTextField(master, height=6, width=100, is_modifiable=True)
                organizer.to_grid(root=master, target=widget)

                self.data_elements[element] = widget

    def data_receive(self, new_data):
        """ Updates Popup fields basing on provided dictionary,
            the dictionary must have keys matching names of fields """

        for element in self.data_elements.items():
            if element[0] in new_data.keys():
                element[1].update_field(new_data[element[0]])
            else:
                # Each field without a matching key in the dictionary displays "No data" info
                element[1].update_field(LONG_TEXT['noData'])

    def data_provide(self):
        """ Returns values provided in frame's entries """

        for name, widget in self.data_elements.items():
            yield name, widget.data_from_field()


def main():
    """If the module is called as __main__, a test run of the popup will be performed."""

    root = tk.Tk()
    root.title('Test - Main Window')
    root.geometry('300x400')

    some_data = {
                   'name':'It is a name.',
                   'problem':'It is a problem.',
                   'solution':'But there is a solution!',
    }

    a = PopupUpdate(root=root, action=lambda x:print(*x, sep='\n'))
    a.data_receive(some_data)

    root.mainloop()


if __name__ == '__main__':
    main()
