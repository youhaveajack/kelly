# -*- coding: utf-8 -*-

""""
kelly.base
~~~~~~~~~~

Base model & property classes.

"""


class Model(object):
    """Base model class - only used to provide a signature"""

    _model_properties = {}
    _model_validators = []

    def __new__(cls, **kwargs):
        return super(Model, cls).__new__(cls)

    def __init__(self, **kwargs):
        super(Model, self).__init__()

    def validate(self):
        pass


class Property(object):
    """Base property class - only used to provide a signature"""

    pass
