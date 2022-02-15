"""
Local API
"""


class Model:
    def __new__(cls, *args, **kwargs):
        return type(cls.__name__, (object,), {})
