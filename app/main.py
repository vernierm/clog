import argparse
import sys

from app.commands.cmd_create import cmd_create
from app.commands.cmd_init import cmd_init
from app.commands.cmd_ls import cmd_ls
from app.commands.cmd_write import cmd_write
from app.util.const import COMMON

arg_parser = argparse.ArgumentParser(description='CLI logging tool')

arg_subparsers = arg_parser.add_subparsers(title='Commands', dest='command')
arg_subparsers.required = True

init_parser = arg_subparsers.add_parser(name="init", help='Initialize logging repo')

ls_parser = arg_subparsers.add_parser(name='ls', help='List all log files')

create_parser = arg_subparsers.add_parser(name='create', help='Create new logging file')
create_parser.add_argument('name', nargs='?', help='representing the file name')

write_parser = arg_subparsers.add_parser(name='write', help='Writes log in specified log file')
write_parser.add_argument('-n', '--name', nargs='?', help='representing the file name',
                          default=COMMON)
write_parser.add_argument('text', nargs='?', help='representing the log input')


def main():
    argv = sys.argv[1:]
    args = arg_parser.parse_args(argv)
    try:
        if args.command == "init":
            cmd_init()
        elif args.command == "ls":
            cmd_ls()
        elif args.command == 'create':
            cmd_create(args.name)
        elif args.command == 'write':
            cmd_write(args.name, args.text)
    except Exception as e:
        print('failed to execute command because: {}'.format(e))
