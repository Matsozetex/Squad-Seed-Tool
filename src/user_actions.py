"""
All user actions as an interface for either interface to use.
"""
from file_handler import FileHandler
from launch_squad import run_squad
from patcher import patch_movies
from const import SEED_MODE, NORMAL_MODE

def get_file_status(handler: FileHandler) -> list:
    """
    Retrieves file statuses.
    """
    return {'s': handler.does_ini_file_exist(SEED_MODE),
            'n': handler.does_ini_file_exist(NORMAL_MODE)}

def make_seed(handler: FileHandler):
    """
    Make the seed ini.
    """
    handler.create_seed_ini()

def make_normal(handler: FileHandler):
    """
    Make the normal ini.
    """
    print ("Are you sure you want to make/overwrite your current normal file?")
    if input("Yes or No? ")[0].lower == "y":  
        handler.create_normal_ini()
    else:
        print("Change exited.")

def run_seed(handler: FileHandler):
    """
    Run seed.
    """
    handler.switch_ini(SEED_MODE)
    run_squad()
    print("Running squad in Seed mode")

def run_normal(handler: FileHandler):
    """
    Run normal.
    """
    handler.switch_ini(NORMAL_MODE)
    run_squad()
    print("Running squad in Seed mode")

def run_patcher():
    """
    Run the file patcher for movies.
    """
    if patch_movies():
        print("Movies patched successfully")
    else:
        print("Movies failed to patch")
