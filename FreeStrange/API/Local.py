"""
Local API
"""


class Mapping:
    def __init__(self):
        self.interrupter = None
        self.code = []

    def print(self, other):
        self.code.append('print ' + other)

    def save(self, other):
        self.code.append('save ' + other)

    def excuse(self):
        self.interrupter(self.code)


class Model:
    def __new__(cls, *args, **kwargs):
        print(args[2].append())
        return type(cls.__name__, (Mapping, ), args[2])
