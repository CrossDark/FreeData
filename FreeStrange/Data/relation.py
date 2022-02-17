"""
relation
"""


class Node:
    def __init__(self, info=None):
        self.info = info
        self.point = []

    def __add__(self, other):
        self.point.append(other)


class Manager:
    def __init__(self, data: {}):
        for k, v in data.items():
            if v is dict:
                self.__init__(v)
            exec('self.' + k + ' = Node("' + v + '")')
