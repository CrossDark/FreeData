"""
Processor
"""
import io
import sqlite3

import click

from .VM import VirtualMachine, Preprocessor, Strange
import os


class Engine:
    def __init__(self, code, strange='not file', mode='r+'):
        if os.path.isfile(strange):
            file = open(strange, mode)
        elif type(strange) is sqlite3.Cursor:
            raise ValueError('sqlite not support')
        elif type(strange) is Strange:
            file = strange
        else:
            file = None
        for i in code:
            VirtualMachine(Preprocessor([self.type(x) for x in i.split(' ')]).out, file).run()
        if file is io.TextIOWrapper or io.BufferedRandom:
            file.close()

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
