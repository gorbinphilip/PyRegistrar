from .registrar import Field


class Model(object):
    """provides abstract model class for implementing different models"""

    def __init__(self):
        raise NotImplementedError()

    def set(self, field_id, value):
        raise NotImplementedError()

    def get(self, field_id):
        raise NotImplementedError()

    def get_list_fields(self):
        raise NotImplementedError()


class Alien(Model):
    """Model for the alien object which can hold alien details"""

    def __init__(self):
        """initializes alien with required fields"""
        self.fields=[]
        self.fields.append(Field("code_name", "Code Name", Field.TYPE_TEXT_ONELINE, "Name detail of the Alien"))
        self.fields.append(Field("blood_color", "Blood Colour", Field.TYPE_TEXT_ONELINE, "Colour of the blood"))
        self.fields.append(Field("no_antenna", "No.s  antenna", Field.TYPE_NUMBER, "Number of antenna"))
        self.fields.append(Field("no_legs", "No.s  legs", Field.TYPE_NUMBER, "Number of legs"))
        self.fields.append(Field("home_planet", "Home Planet", Field.TYPE_NUMBER, "Name of the home planet"))

    def set(self, field_id, value):
        self.field_id=value

    def get(self, field_id):
        return self.field_id

    def get_list_fields(self):
        return self.fields
