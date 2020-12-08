from argparse import ArgumentParser

class Command():
    parser = ArgumentParser(description='A CLI for interacting with New Relic\'s API')
    subparser = parser.add_subparsers(description='Available resources', dest='command')

    def __init__(self):
        print('Command.__init__()')