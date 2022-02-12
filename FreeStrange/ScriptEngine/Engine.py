"""
Processor
"""
from . import keyword_list, wait_list


class Preprocessor:
    def __init__(self, code):
        self.stack = []
        self.out = []
        wait = []
        for i in code:
            if len(wait) != 0:
                self.out += self.stack
                self.out.append(i)
                self.out += wait
                wait.pop()
            elif (i in keyword_list) and (i in wait_list):
                wait.append(i)
            elif (i in keyword_list) and (i not in wait_list):
                self.out.append(i)
            else:
                self.stack.append(i)
