from cli.command import Command
from cli.resource import ExampleResource

class ExampleCommand(Command):
    parser = Command.subparser.add_parser('set', help='Manage values')
    subparser = parser.add_subparsers(help='Supported actions', dest='set')

    def __init__(self):
        print('ExampleCommand __init__()')

        super().__init__()

        self.resource = ExampleResource()

    def process_command(self):
        print('Called ExampleCommand.process_command')

        for subclass in ExampleCommand.__subclasses__():
            subclass().process_command()