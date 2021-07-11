# This program extends multi-clipboard program found in Automate the Boring Stuff with Python,
# giving it a delete function. It adds a delete <keyword> command line argument that will delete a keyword
# from the shelf. Then, it adds a delete command line argument that will delete all of the keywords.

#! python3
# mcb.pyw - Saves and loads pieces of test to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword to clipboard.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.


import pyperclip
import shelve
import sys

mcbShelf = shelve.open('mcb')

# Save keyword in clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# Delete keyword in clipboard content.
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]


elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    # Deletes all items in clipboard
    elif sys.argv[1] == 'delete':
        for keyword in list(mcbShelf.keys()):
            del mcbShelf[keyword]


mcbShelf.close()



