"""
Runs the seeding application.
"""

import os
import sys
from file_handler import FileHandler
import args_interface
import cli_interface

def main():
    """
        Runs the main menu of the app.
    """
    ini_dir = FileHandler()
    if len(sys.argv) > 1:
        args_interface.argument_logic(sys.argv, ini_dir)
    else:
        try:
            cli_interface.menu_handler(ini_dir)
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt detected, closing tool.")
            os._exit(0)

if __name__ == "__main__":
    main()
