from cli.command import Command
from cli.resource import ExampleResource

class GetCommand(Command):
    parser = Command.subparser.add_parser('get', help='Get values')
    subparser = parser.add_subparsers(help='Supported get actions', dest='get')

    def __init__(self):
        super().__init__()

        self.resource = ExampleResource()

    def process_command(self, args):
        pass

    def can_handle(self, args):
        return args.command == 'get' and args.get == None