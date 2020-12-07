from cli.command import ExampleCommand

class ExampleSubcommand(ExampleCommand):


    def __init__(self):
        print('ExampleSubcommand.__init__()')

        super().__init__()

        

    def process_command(self):
        print('ExampleSubcommand.process_command()')

        self.resource.process_resource()