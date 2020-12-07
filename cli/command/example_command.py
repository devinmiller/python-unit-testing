from cli.command import Command
from cli.resource import ExampleResource

class ExampleCommand(Command):
    root = Command.parser.add_parser('set', help='Manage values')
    parser = root.add_subparsers(help='Supported actions', dest='set')

    @classmethod
    def build_command(cls, parser):
        pass

    def __init__(self):
        print('ExampleCommand __init__()')

        super().__init__()

        self.resource = ExampleResource()

    def process_command(self):
        print('Called ExampleCommand.process_command')

        for subclass in ExampleCommand.__subclasses__():
            subclass().process_command()