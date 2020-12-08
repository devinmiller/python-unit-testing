from cli.command import GetCommand
from cli.resource import ExampleResource

class GetConfigurationCommand(GetCommand):
    parser = GetCommand.subparser.add_parser('configuration', help='Get configuration value')
    
    def __init__(self):
        super().__init__()

        self.resource = ExampleResource()

    def process_command(self, args):
        pass

    def can_handle(self, args):
        return args.get == 'configuration'