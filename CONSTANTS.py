#!/usr/bin/python3

"""Those are Human-readable Text Constants, stored in one place for easy management and eventual translation"""


"""About program text"""

ABOUT_PROGRAM = """What does this program do?
This program allows you to store solutions and descriptions of problems.

I've found that I sometimes encounter the same problems and end up 
searching for solutions that I've previously discovered (but i forgot about them). 
This kills my productivity (and my good mood) so I made this program as a solution.  

Maybe it is not a very impressive program to showcase
but at least it is not just another calculator.
Plus it actually has something to do with the real-life problem!
"""

"""Texts constants"""

LONG_TEXT = {
    'about':        'About program',
    'add':          'Add entry',
    'allFiles':     'All files',
    'con_del':      'Please, confirm deletion of following data: ',
    'confirm':      'Confirm the action',
    'create':       'Create database',
    'change':       'Change database',
    'changeLang':   'Change language',
    'currentEdit':  'Currently editing: ',
    'dbFiles':      'Database files',
    'delete':       'Delete entry',
    'load':         'Load database',
    'new':          'New database',
    'noData':       '- No data -',
    'programTitle': 'Solutions Database',
    'select':       'Select database',
    'selectLang':   'Select language: ',
    'update':       'Update entry',
}

ERROR_TEXT = {
    'existTitle':           'File already exists',
    'existMessage':         'File with that name already exists.',
    'noNameTitle':          'No name',
    'noNameMessage':        'Please enter a name for a database.',
    'notFoundTitle':        'File not found',
    'notFoundMessage':      'File not found.\nPlease make sure the spelling is correct.',
    'validTitle':           'Not a valid database',
    'validMessage':         'This file is not a valid database for this program.',
    'dataSetNameTitle':     'Name error',
    'dataSetNameMessage':   'Data set with that name already exists.',
}

"""Single words constants"""

ADD         = 'Add'
ANSWERS     = 'Answers'
CANCEL      = 'Cancel'
CHANGE      = 'Change'
CREATE      = 'Create'
CONFIRM     = 'Confirm'
DATA        = 'Data'
DELETE      = 'Delete'
EDIT        = 'Edit'
EXIT        = 'Exit'
FILE        = 'File'
FIND        = 'Find...'
GOALS       = 'Goals'
HELP        = 'Help'
HI          = 'Hi!'
NAME        = 'Name'
NAVIGATION  = 'Navigation'
PROBLEM     = 'Problem'
REFRESH     = 'Refresh'
SELECT      = 'Select'
SETTINGS    = 'Settings'
SHORTCUTS   = 'Shortcuts'
SOLUTION    = 'Solution'
TASK        = 'Task'
WARNING     = 'Warning!'
UPDATE      = 'Update'

"""Below constants should NOT be translated, some program functions depend on them"""

ENGLISH     = 'English (Implemented)'
POLISH      = 'Polish (Nie zaimplementowano)'
SPANISH     = 'Spanish (No se ha implementado)'

SEPARATOR = 'separator'
