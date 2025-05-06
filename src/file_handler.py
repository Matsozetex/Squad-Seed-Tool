"""
Handles all interaction with Squad ini files.
"""

import os
import logging
import shutil
import pathlib

from const import (NORMAL_SETTINGS_FILE, SEED_SETTINGS_FILE,
                       GAME_SETTINGS_FILE, SETTINGS_DATA, SEED_MODE, NORMAL_MODE)

SETTING_DIRECTORY = (pathlib.Path(os.getenv('LOCALAPPDATA'))) / 'SquadGame' / \
    'Saved' / 'Config' / 'WindowsNoEditor'

class FileHandler:
    """
    1. Check the current file type.

    2. Switch files.

    3. Create/Update the normal file.

    4. Create seed file.
    """
    def __init__(self) -> None:
        self.dir = SETTING_DIRECTORY
        self.game = os.path.join(SETTING_DIRECTORY, GAME_SETTINGS_FILE)
        self.seed = os.path.join(SETTING_DIRECTORY, SEED_SETTINGS_FILE)
        self.normal = os.path.join(SETTING_DIRECTORY, NORMAL_SETTINGS_FILE)
        self.settings = SETTINGS_DATA

    def does_ini_file_exist(self, mode) -> bool:
        """
        Check if a file of a specified type exists.
        """
        does_exist = False
        if mode == SEED_MODE:
            does_exist = os.path.exists(self.seed)
        elif mode == NORMAL_MODE:
            does_exist = os.path.exists(self.normal)
        else:
            does_exist = False
            logging.warning("Inputted mode does not exist: %s", mode)

        return does_exist

    def switch_ini(self, mode: str) -> None:
        """
        Switch between modes.
        """
        if mode.lower() in NORMAL_MODE:
            new_ini_path = self.normal
        elif mode.lower() in SEED_MODE:
            new_ini_path = self.seed
        else:
            logging.error("Invalid mode of: %s", mode)
            os._exit(1)

        if(os.path.exists(self.normal) and os.path.exists(self.seed)):
            os.remove(self.game)
            shutil.copy(new_ini_path, self.game)
        else:
            logging.warning("Seed or Normal file is missing, fix it!")

    def create_normal_ini(self) -> None:
        """
        Creates new normal file or updates it.
        """
        if is_seed_ini(self.game) is False:
            shutil.copy(self.game, self.normal)
        else:
            logging.warning("Current mode is seed, cannot create new file!")

    def create_seed_ini(self):
        """
        Creates new SEED file if one doesn't already exist.
        """
        with open(self.seed, "w", encoding="UTF-8") as file:
            file.write(self.settings)

def is_seed_ini(file_path) -> bool:
    """
    Check if the current game ini is a seed ini.
    """
    is_seed = False
    with open(file_path, "r", encoding="UTF-8") as file:
        if ";SEED_MODE" in file:
            is_seed = True
    return is_seed
