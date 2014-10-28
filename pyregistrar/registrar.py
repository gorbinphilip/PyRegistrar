


class Field(object):
    """Provides standard fields to represent attributes"""
    TYPE_NONE="none"
    TYPE_NUMBER="number"
    TYPE_TEXT_ONELINE="text:oneline"
    TYPE_TEXT_MULTILINE="text:multiline"
    TYPE_TEXT_PASSWORD="text:password"
    
    def __init__(self, field_id, field_name, field_type, description=None):
        self.field_id=field_id
        self.field_name=field_name
        self.field_type=field_type
        self.field_description=description

