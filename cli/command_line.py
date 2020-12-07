from cli.command import Command

def main():

    for subclass in Command.__subclasses__():
        command = subclass()
        command.process_command()