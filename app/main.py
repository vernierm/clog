import argparse
import sys

from app.commands.cmd_init import cmd_init
from app.commands.cmd_ls import cmd_ls

arg_parser = argparse.ArgumentParser(description="CLI logging tool")

arg_subparsers = arg_parser.add_subparsers(title="Commands", dest="command")
arg_subparsers.required = True

init_parser = arg_subparsers.add_parser(name="init", help="Initialize logging repo")

ls_parser = arg_subparsers.add_parser(name='ls', help='List all log files')


def main(argv=sys.argv[1:]):
    args = arg_parser.parse_args(argv)
    try:
        if args.command == "init":
            cmd_init()
        elif args.command == "ls":
            cmd_ls(args)
    except Exception as e:
        print('failed to execute command because: {}'.format(e))
