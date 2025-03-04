"""
Defines behaviour of argument controls.
"""

import argparse
import user_actions
from file_handler import FileHandler
from src.const import SEED_MODE, NORMAL_MODE

def argument_handler()-> None:
    """
    Defines arguments for running the script and parses them.
    """
    parser = argparse.ArgumentParser(
            prog="seedtoolv2",
            description="a program that manages alternate setting profiles for Squad seeding"
        )
    group = parser.add_argument_group(
        'file operation commands', 
        'commands that execute file operations to faciltiate squad seeding'
        )
    exclusive_group = group.add_mutually_exclusive_group(required=True)
    exclusive_group.add_argument(
        '-m',
        '--make', 
        type=str,
        choices=[SEED_MODE, NORMAL_MODE],
        help='make or update/reset the alternate profiles'
        )
    exclusive_group.add_argument(
        '-r', 
        '--run', 
        type=str,
        choices=[SEED_MODE, NORMAL_MODE],
        help='run the game in the alternate mode'
        )
    exclusive_group.add_argument(
        '-s',
        '--status',
        help='checks status of alternate profiles',
        action='store_const',
        const=1
    )
    exclusive_group.add_argument(
        '-p',
        '--patch',
        help='patches the Movies folder to skip startup cinematics',
        action='store_const',
        const=1
    )
    args = parser.parse_args()
    return args

def argument_logic(args, handler: FileHandler) -> None:
    """
    Defines switching logic with related functions.
    """
    args = argument_handler()
    if args.make is not None:
        if args.make == NORMAL_MODE:
            user_actions.make_normal(handler)
        elif args.make == SEED_MODE:
            user_actions.make_seed(handler)
    elif args.run is not None:
        if args.run == NORMAL_MODE:
            user_actions.run_normal(handler)
        elif args.run == SEED_MODE:
            user_actions.run_seed(handler)
    elif args.status is not None:
        status = user_actions.get_file_status(handler)
        print(f"Seed exists: {status['s']} | Normal exists: {status['n']}")
    elif args.patch is not None:
        user_actions.run_patcher()