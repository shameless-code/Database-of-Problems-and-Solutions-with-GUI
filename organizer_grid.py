#!/usr/bin/python3

# Native Python imports
from tkinter import Grid


class OrganizerGrid:
    """ Places widgets on the grid in provided root window/frame,
        makes life a little easier """

    def __init__(self):
        self.row_count = 0
        self.column_count = 0

    def to_grid(
            self,
            root=None,
            target=None,
            sticky='nsew',
            scalable=True,
    ):
        target.grid(row=self.row_count, column=self.column_count, sticky=sticky)
        if scalable is True:
            # Those two lines below allows an output to scale with the window
            Grid.columnconfigure(root, self.column_count, weight=1)
            Grid.rowconfigure(root, self.row_count, weight=1)

        self.row_count += 1
