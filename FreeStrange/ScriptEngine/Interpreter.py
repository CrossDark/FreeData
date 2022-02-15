"""
Processor
"""
import click

from .VM import VirtualMachine, Preprocessor
import os


class Engine:
    def __init__(self, code, strange=None):
        if os.path.isfile(strange):
            with open(strange, 'r+') as file:
                for i in code:
                    VirtualMachine(Preprocessor([self.type(x) for x in i.split(' ')]).out, file).run()
        else:
            for i in code:
                VirtualMachine(Preprocessor([self.type(x) for x in i.split(' ')]).out).run()

    @staticmethod
    def type(get):
        try:
            return int(get)
        except ValueError:
            return get


class CLI:
    def __init__(self):
        pass

    @staticmethod
    @click.command()
    @click.option(
        '--get', prompt='FreeData>>'
    )
    def main(get):
        VirtualMachine(Preprocessor([Engine.type(x) for x in get.split(' ')]).out).run()
        CLI.main()
