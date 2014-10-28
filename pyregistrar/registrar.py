class Field(object):
    """Provides standard fields to represent attributes"""
    TYPE_NONE="none"
    TYPE_NUMBER="number"
    TYPE_TEXT_ONELINE="text:oneline"
    TYPE_TEXT_MULTILINE="text:multiline"
    TYPE_TEXT_PASSWORD="text:password"
    
    def __init__(self, field_id, field_name, field_type, description=None):
        """initializes with required attributes"""
        self.field_id=field_id
        self.field_name=field_name
        self.field_type=field_type
        self.field_description=description

from . import models

def register(model, file_name, file_ext):
    pass


def get_models():
    """returns list of available models"""
    return models.__all_models__


def get_extensions():
    """returns list of available output file formats"""
    pass
