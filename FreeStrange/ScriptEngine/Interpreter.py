"""
Processor
"""
from .VM import VirtualMachine, Preprocessor


class Engine:
    def __init__(self, code):
        for i in code:
            VirtualMachine(Preprocessor([self.type(x) for x in i.split(' ')]).out).run()

    @staticmethod
    def type(get):
        try:
            return int(get)
        except ValueError:
            return get
