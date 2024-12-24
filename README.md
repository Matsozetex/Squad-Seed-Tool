# sneedtoolv2
The simpler seed tool that doesn't require a PHD to operate. 

Key features incldue:
- Reduced file size ~148 MB -> ~5 MB
- Less user input required for script to function
- Open source

## Using the Tool

### Set Up
If you are a new user to any seed tool, this tool is plug and play.

If you have previously used the older seeding tool, you need to ensure the following:
- Restore your game ini to your normal play version of the file
- Delete any other alternate ini files, such as SeedGameUserSettings.ini and NormalGameUserSettings.ini


### Tool Options
To run the tool, simply double click on the tool in File Explorer or run the tool from command line. Then you have the following options:
- 0: Exit the tool
- 1: Make new seed file **(Exist: True is Required)**: Makes a settings file with low power options enabled.
- 2: Make/update normal file **(Exist: True is Required)**: Backups your settings file with your normal options.
- 3: Run the game with seed settings: Launches Squad with low power options enabled.
- 4: Run the game with normal settings: Launches Squad with normal options.
- 5: Patch the game to remove the startup movies.

## Advanced Topics
### Adding to Path
For advanced users who use Windows terminal frequently. You can add this tool to your path to execute the script from any location [by following this guide](https://stackoverflow.com/questions/4822400/register-an-exe-so-you-can-run-it-from-any-command-line-in-windows).

### Running Using Args
An extension to the above would be running the program using arguments, so that you can assign shortcuts to execute the program or simply execute without the interface.

Arguments can be accessed by putting the ```--help``` flag to read the manual page on it.

### Compiling Yourself
If any of this is suspicious to you, you either hadn't used any of my previous seeding tools or you know not to run random software off the internet.

Compilation is easy, follow these steps:
1. Install Python version 3.10 or greater.
2. Install pyinstaller using pip(3).
3. Run the following pyinstaller command within the directory of main.py:
```pyinstaller -F --paths . -n squad.exe --hiddenimport=pyautogui .\main.py```
