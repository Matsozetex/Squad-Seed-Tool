"""
Handles all interaction with Squad ini files.
"""

import os
import logging
import shutil
import const
import re

class FileHandler:
    """
    1. Check the current file type.

    2. Switch files.

    3. Create/Update the normal file.

    4. Create seed file.
    """
    def __init__(self) -> None:
        self.dir = const.DIR
        self.game = os.path.join(const.DIR, const.GAME)
        self.seed = os.path.join(const.DIR, const.SEED)
        self.normal = os.path.join(const.DIR, const.NORMAL)
        self.settings = const.SETTINGS

    def does_ini_file_exist(self, mode) -> bool:
        """
        Check if a file of a specified type exists.
        """
        does_exist = False
        if mode == "seed":
            does_exist = os.path.exists(self.seed)
        elif mode == "normal":
            does_exist = os.path.exists(self.normal)
        else:
            does_exist = False
            logging.warning("Inputted mode does not exist: %s", mode)

        return does_exist

    def switch_ini(self, mode: str) -> None:
        """
        Switch between modes.
        """
        if mode.lower() in "normal":
            new_ini_path = self.normal
        elif mode.lower() in "seed":
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

    def get_server_name(self) -> str:
        """
        Finds the desired server name
        """
        server_name = ""
        if os.path.isfile(self.seed):
            with open(self.seed, "r+", encoding="UTF-8") as file:
                first_line=file.readline()
                match = re.search("^server_name=(.*)$", first_line)
                if match is not None:
                    server_name =  match.group()[12:]
                else:
                    server_name = 'None'
        else:
            server_name = 'None'
        return server_name

def is_seed_ini(file_path) -> bool:
    """
    Check if the current game ini is a seed ini.
    """
    is_seed = False
    with open(file_path, "r", encoding="UTF-8") as file:
        if ";SEED_MODE" in file:
            is_seed = True
    return is_seed
