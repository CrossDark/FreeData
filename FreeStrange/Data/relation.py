"""
relation
"""


class Node:
    def __init__(self, info=None):
        self.info = info
        self.point = []

    def __add__(self, other):
        self.point.append(other)
