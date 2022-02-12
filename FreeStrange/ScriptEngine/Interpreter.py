"""
Processor
"""
from .VM import VirtualMachine, Preprocessor


class Engine:
    def __init__(self, code):
        for i in code:
            VirtualMachine(Preprocessor(i.split(' ')).out).run()
