from argparse import ArgumentParser
from pprint import pp
from cli.command import Command, GetCommand, GetConfigurationCommand

def configure_command(command):
    pass

def process_command(command):
    pass

def main():


    get_command = GetCommand()
    get_configuration_command = GetConfigurationCommand()

    args = Command.parser.parse_args()

    print(args)