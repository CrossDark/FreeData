"""
Script Engine
"""


class VirtualMachine:
    def __init__(self, code):
        self.code = code
        self.stack = []
        self.address = 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    @property
    def top(self):
        return self.stack[-1]

    def dispatch(self, opcode):
        dispatch_map = {
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
            "=": self.value
        }
        if opcode in dispatch_map:
            dispatch_map[opcode]()
        elif isinstance(opcode, int):
            self.push(opcode)
        elif isinstance(opcode, str) \
                and opcode[0] == opcode[-1] == '"':
            self.push(opcode[1:-1])

    def run(self):
        while self.address < len(self.code):
            opcode = self.code[self.address]
            self.address += 1
            self.dispatch(opcode)

    # base functions
    def mod(self):
        pass

    def mul(self):
        v2 = self.pop()
        v1 = self.pop()
        self.push(v1 * v2)

    def plus(self):
        v2 = self.pop()
        v1 = self.pop()
        self.push(v1 + v2)

    def minus(self):
        pass

    def div(self):
        pass

    def eq(self):
        pass

    def cast_int(self):
        pass

    def cast_str(self):
        pass

    def drop(self):
        pass

    def dup(self):
        pass

    @staticmethod
    def exit():
        exit()

    def if_stmt(self):
        pass

    def jmp(self):
        address = self.pop()
        if 0 <= address < len(self.code):
            self.address = address
        else:
            raise RuntimeError("address must be integer")

    def over(self):
        pass

    def print(self):
        print(self.stack.pop())

    def print_in(self):
        print(int(self.stack[-1]))

    def read(self):
        pass

    def dump_stack(self):
        pass

    def swap(self):
        pass

    # data function
    def value(self):
        v2 = self.pop()
        v1 = self.pop()
        exec(v1 + '=' + v2)
