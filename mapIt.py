#!/usr/bin/env python3

import webbrowser, sys, pyperclip

def mapIt():
    """Open location from a clipboard or terminal in the browser"""
    if len(sys.argv) > 1:
        # get the address
        address = ' '.join(sys.argv[1:])
        # open the browser page and map the address
        webbrowser.open('https://www.google.com/maps/place/' + address)

    else:
        # retrieve text from clipboard
        clipboard_content = pyperclip.paste().strip() #remove leading and trailing white spaces
        print(clipboard_content)
        if clipboard_content:
            # split address by new line
            addresses = clipboard_content.split('\n')
            for address in addresses:
                webbrowser.open('https://www.google.com/maps/place/' + address.strip())

        else:
            print("No address provided")


    

if __name__ == "__main__":
    # runs this function when script is run directly

    mapIt()

    # sudo ln -s /Desktop/development/webscraping/mapIt/mapIt.py /usr/local/bin/mapit
