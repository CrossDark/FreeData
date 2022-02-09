"""
Operating data
"""


class Record:
    def __init__(self, path, *title):
        super(Record, self).__init__()
        try:
            self.Form = open(path, 'r+')
        except FileNotFoundError:
            self.Form = open(path, 'w').close()
            self.Form = open(path, 'r+')
            self.Form.write('')
            for i in title:
                self.Form.write('' + i + '')
            self.Form.seek(0, 2)
            self.Form.write('' + chr(10))

    def __enter__(self):
        self.Data = [i.replace('', '').replace(chr(10), '').split('')[1:-1:2] for i in self.Form.readlines()[1:]]
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Form.close()

    def __add__(self, other: list):
        self.Form.write(chr(29))
        for i in other:
            self.Form.write('' + i + '')
        self.Form.write(chr(29) + chr(10))
