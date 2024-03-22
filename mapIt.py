#!/usr/bin/env python3

import webbrowser, sys, pyperclip

def mapIt():
    """Open location from a clipboard or terminal in the browser"""
    if len(sys.argv) > 1:
        # get the address
        address = ' '.join(sys.argv[1:])

    else:
        # get address from clipboard
        address = pyperclip.paste()

    webbrowser.open('https://www.google.com/maps/place/' + address)

if __name__ == "__main__":
    mapIt()

    # sudo ln -s /Desktop/development/webscraping/mapIt/mapIt.py /usr/local/bin/mapit
