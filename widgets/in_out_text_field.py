#!/usr/bin/python3

# Native Python imports
import tkinter as tk
from tkinter import scrolledtext


class UpdateTextField:
    """ Created for use with InOutTextField
        Updates the text field """

    @staticmethod
    def update_no_write_field(target, new_content):
        """ Allows to update a NO is_modifiable for user text field """

        target.config(state='normal')
        target.delete('1.0', tk.END)
        target.insert(tk.END, new_content)
        target.config(state='disabled')

    @staticmethod
    def update(target, new_content):
        """ Allows to update an is_modifiable for user text field """

        target.delete('1.0', tk.END)
        target.insert(tk.END, new_content)


class GetTextField:
    """ Grabs data from tkinter text fields """

    @staticmethod
    def get(target):
        return target.get("1.0", tk.END).strip()   # .strip() because by default adds "\n" to the end


class InOutTextField(scrolledtext.ScrolledText):
    """ Slightly modified ScrolledText widget to make it more convenient as output/entry field """

    def __init__(
            self,
            root=None,
            height=1,
            width=10,
            is_modifiable=False,
            update=UpdateTextField(),
            send=GetTextField(),
    ):
        super().__init__(root, height=height, width=width, wrap='word')
        self.is_modifiable = is_modifiable
        self.update = update
        self.send = send

        if self.is_modifiable is False:
            # For some systems copy-paste became disabled after setting widget state to "disabled"
            # Line below fixes this problem
            self.bind("<Button>", lambda event: self.focus_set())
            self.config(state='disabled')
            self.config(background='lightgrey')

    def update_field(self, new_content):
        """ Updates the text field, there are separate methods for is_modifiable and not is_modifiable fields """

        if self.is_modifiable is False:
            self.update.update_no_write_field(self, new_content)
        else:
            self.update.update(self, new_content)

    def data_from_field(self):
        """Extracts data from the text field"""

        return self.send.get(self)


def main():
    """If the module is called as __main__, a test run of the widget will be performed."""

    root = tk.Tk()
    root.geometry('300x300')

    # Modifiable for user text field
    field1 = InOutTextField(root=root, is_modifiable=True)
    field1.pack(fill='both', expand=True, padx=5, pady=5)

    # No modifiable for user text field
    field2 = InOutTextField(root=root, is_modifiable=False)
    field2.update_field('Try to copy me!')
    field2.pack(fill='both', expand=True, padx=5, pady=5)

    root.mainloop()


if __name__ == '__main__':
    main()
