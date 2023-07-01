#!/usr/bin/python3

# Native Python imports
import tkinter as tk

# Project-specific imports
from CONSTANTS import *


class ConstructorMenuBar:
    """ Creates Menu Bar basing on provided list of Tabs and list of Actions """

    def __init__(self, root, list_tabs):
        """ Expects dict(dict()) {idName:{nameTab:str(), listOptions:dict(dict())}}
            Each tab should have own listOptions dict(dict()) with a structure:
            {idName:{nameOption:str(), command:lambda: function()}} """

        # Creating Menu Bar
        menu = tk.Menu(root, tearoff=0)

        # Creating tabs and options based on menuTabsList
        for tab in list_tabs.values():
            menu_tab = tk.Menu(menu, tearoff=0)
            menu.add_cascade(menu=menu_tab, label=tab['nameTab'])
            for option in tab['listOptions'].values():
                if option['nameOption'] == 'separator':
                    menu_tab.add_separator()
                else:
                    menu_tab.add_command(label=option['nameOption'], command=option['command'])

        # Assigning Menu Bar to root
        root.config(menu=menu)


def main():
    """If the module is called as __main__, a test run of the Menu Bar Constructor will be performed."""
    root = tk.Tk()
    root.geometry('300x400')

    # Creating list of tabs for Menu Bar
    editTab = {
        'add': {'nameOption': ADD, 'command': lambda: print(ADD)},
        'sep1': {'nameOption': SEPARATOR, },
        'update': {'nameOption': UPDATE, 'command': lambda: print(UPDATE)},
        'sep2': {'nameOption': SEPARATOR, },
        'delete': {'nameOption': DELETE, 'command': lambda: print(DELETE)},
    }

    fileTab = {
        'change': {'nameOption': LONG_TEXT['change'], 'command': lambda: print(LONG_TEXT['change'])},
        'sep1': {'nameOption': SEPARATOR, },
        'exit': {'nameOption': EXIT, 'command': lambda: root.destroy()},
    }

    menuTabsList = {
        'file': {'nameTab': FILE, 'listOptions': fileTab, },
        'edit': {'nameTab': EDIT, 'listOptions': editTab, },
    }

    # Creating Menu Bar
    ConstructorMenuBar(root, menuTabsList)

    root.mainloop()


if __name__ == '__main__':
    main()
