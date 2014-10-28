from .registrar import Field


class Model(object):
    """provides abstract model class for implementing different models"""

    def __init__(self):
        raise NotImplementedError()

    def set(self, field, value):
        raise NotImplementedError()

    def get(self, field):
        raise NotImplementedError()

    def get_list_fields(self):
        raise NotImplementedError()
