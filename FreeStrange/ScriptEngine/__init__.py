"""
Script Engine
"""
keyword_list = [
    # Base
    '%', '*', '+', '-', '/', '==', 'cast_int', 'cast_str', 'drop', 'dup', 'exit', 'if', 'jmp', 'over',
    'print', 'println', 'read', 'stack', 'swap', 'node',
    # Data
    '=', 'show', 'save', 'use', 'pickle'
]
wait_list = ['+', '-', '*', '/', '==', 'swap']
start_end_list = ['print', 'printIn', 'save', 'node', 'pickle']


class BaseMachine:
    def __init__(self):
        self.dispatch_map = {
            # Base
            "%": self.mod,
            "*": self.mul,
            "+": self.plus,
            "-": self.minus,
            "/": self.div,
            "==": self.eq,
            "cast_int": self.cast_int,
            "cast_str": self.cast_str,
            "drop": self.drop,
            "dup": self.dup,
            "exit": self.exit,
            "if": self.if_stmt,
            "jmp": self.jmp,
            "over": self.over,
            "print": self.print,
            "println": self.print_in,
            "read": self.read,
            "stack": self.dump_stack,
            "swap": self.swap,
            "node": self.node
        }

    def mod(self): pass

    def mul(self): pass

    def plus(self): pass

    def minus(self): pass

    def div(self): pass

    def eq(self): pass

    def cast_int(self): pass

    def cast_str(self): pass

    def drop(self): pass

    def dup(self): pass

    @staticmethod
    def exit(): pass

    def if_stmt(self): pass

    def jmp(self): pass

    def over(self): pass

    def print(self): pass

    def print_in(self): pass

    def read(self): pass

    def dump_stack(self): pass

    def swap(self): pass

    def node(self): pass
