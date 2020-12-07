from argparse import ArgumentParser

class Command():
    root = ArgumentParser(description='A CLI for interacting with New Relic\'s API')
    parser = root.add_subparsers(description='Available resources', dest='command')

    def __init__(self):
        print('Command.__init__()')