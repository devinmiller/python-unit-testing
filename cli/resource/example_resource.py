from cli.resource import Resource

class ExampleResource(Resource):
    def __init__(self):
        super().__init__()

        print('ExampleResource __init__()')
        print(self.__module__)

    def process_resource(self):
        print('Called ExampleResource.process_resource')