"""
Processor
"""
import sqlite3

import click

from .VM import VirtualMachine, Preprocessor
import os


class Engine:
    def __init__(self, code, strange='not file'):
        if os.path.isfile(strange):
            with open(strange, 'rb+') as file:
                for i in code:
                    VirtualMachine(Preprocessor([self.type(x) for x in i.split(' ')]).out, file).run()
        elif type(strange) == sqlite3.Cursor:
            raise ValueError('sqlite not support')
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
