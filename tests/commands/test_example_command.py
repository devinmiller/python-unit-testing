import pytest

from cli.command import ExampleCommand

class ResourceMock:
    def process_resource(self, *args, **kwargs):
        print('Called ResourceMock.process_resource')

def test_call_resource(mocker, capsys):
    with capsys.disabled():
        # arrange
        command = ExampleCommand()

        mock_resource = ResourceMock()

        mocker.patch.object(command, 'resource', mock_resource)

        # act
        command.process_command()

