import argparse
import sys

arg_parser = argparse.ArgumentParser(description="The CLI logging tool")

arg_subparsers = arg_parser.add_subparsers(title="Commands", dest="command")
arg_subparsers.required = True

init_parser = arg_subparsers.add_parser(name="init", help="Initialize")
init_parser.add_argument("path", default="~/.clog", help="where to create log base directory")


def main(argv=sys.argv[1:]):
    args = arg_parser.parse_args(argv)
    print (args.command)
