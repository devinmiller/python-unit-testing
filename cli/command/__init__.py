print(__name__)
print(__package__)

from .command import Command

from .get.command import GetCommand
from .get.configuration_command import GetConfigurationCommand

from .example_command import ExampleCommand
from .example_subcommand import ExampleSubcommand