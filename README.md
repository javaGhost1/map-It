# mapIt.py

This script opens a location in Google Maps either from command-line arguments or from the clipboard.

## Usage

Run the script directly from the command line, providing the address as arguments or by copying it to the clipboard.

```bash
python3 mapIt.py 870 Valencia St, San Francisco, CA 94110
```

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/your_repository.git


2. **Create Symbolic Link:**
Navigate to the directory containing mapIt.py and create a symbolic link named mapit pointing to the script:
    ```bash
    ln -s $(pwd)/mapIt.py /usr/local/bin/mapit
    
3. ***Make Script Executable:***
Ensure that the script is executable by running:
    ```bash
    chmod +x /usr/local/bin/mapit

  ## Shebang Line
Make sure to include the following shebang line at the beginning of mapIt.py:
    ```bash
    #!/usr/bin/env python3
The shebang line specifies the Python 3 interpreter, ensuring the script is executed with the correct version of Python.

  ## Usage Example
After completing the installation steps, you can use the mapit command followed by the address directly from the command line:
    
    'mapit 870 Valencia St, San Francisco, CA 94110'
    
This will open the provided address in Google Maps in your default web browser.
