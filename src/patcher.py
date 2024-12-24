"""
Patches Squad to remove all the extra videos as it can break auto-mode.
"""
import winreg
import pathlib
import os
import vdf

def patch_movies() -> bool:
    """
    Run the Squad movie patcher.
    """
    try:
        libraryfolders_config_location = get_steam_config_location()
        squad_install_location = get_squad_install_path(libraryfolders_config_location)
        squad_movies_location = get_squad_movie_path(squad_install_location)
        rename_movie_folder(squad_movies_location)
        return True
    except OSError:
        print(OSError)

def get_steam_config_location() -> str:
    """
    Retrieves the steam base install location from registry.
    """
    registry_handle = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
    steam_key = winreg.OpenKey(registry_handle,                      
                               r"SOFTWARE\WOW6432Node\Valve\Steam", 
                               0,
                               winreg.KEY_READ)
    install_path_key = winreg.QueryValueEx(steam_key, "InstallPath")[0]

    return pathlib.PurePath(install_path_key, "config", "libraryfolders.vdf")

def get_squad_install_path(library_folders: str) -> str:
    """
    Get the install location fro Squad from the libraryfolders.vdf file.
    """
    squad_install_path = ''
    with open(library_folders, 'r', encoding="UTF_8") as file:
        data = vdf.load(file)["libraryfolders"]
        for v_location in data:
            curr_v_location = data.get(v_location)
            for v_app in curr_v_location["apps"]:
                if v_app == "393380":
                    squad_install_path = curr_v_location["path"]
    return squad_install_path

def get_squad_movie_path(squad_steam_path:str) -> str:
    """
    Converts the Squad install directory to the Movies directory.
    """
    movie_path = pathlib.PurePath(squad_steam_path,
                                  "steamapps",
                                  "common",
                                  "Squad",
                                  "SquadGame",
                                  "Content",
                                  "Movies"
                                  )
    return movie_path



def rename_movie_folder(path_to_movies: str) -> None:
    """
    Renames the movie folder that affect startup.
    """
    if pathlib.Path(path_to_movies).exists():
        new_movie_dir = str(path_to_movies) + "_old"
        os.rename(path_to_movies, new_movie_dir)
    else:
        print("Movies directory has already been renamed")
