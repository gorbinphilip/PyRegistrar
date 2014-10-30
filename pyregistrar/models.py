from .fields import Field

__all_models__=["Alien"]  #global variable used to identify available models

class Model(object):
    """
    Provides abstract model class for implementing different models
    """

    def __init__(self):
        raise NotImplementedError()

    def set(self, field_id, value):
        raise NotImplementedError()

    def get(self, field_id):
        raise NotImplementedError()

    def get_list_fields(self):
        raise NotImplementedError()


class Alien(Model):
    """
    Model for the alien object which can hold alien details
    """

    def __init__(self):
        """
        initializes alien with required fields like 'Code Name', 'Blood Colour'.. etc
        """
        self.fields=[]
        self.fields.append(Field("code_name", "Code Name", Field.TYPE_TEXT_ONELINE, "Name detail of the Alien"))
        self.fields.append(Field("blood_color", "Blood Colour", Field.TYPE_TEXT_ONELINE, "Colour of the blood"))
        self.fields.append(Field("no_antenna", "No.s  antenna", Field.TYPE_NUMBER, "Number of antenna"))
        self.fields.append(Field("no_legs", "No.s  legs", Field.TYPE_NUMBER, "Number of legs"))
        self.fields.append(Field("home_planet", "Home Planet", Field.TYPE_TEXT_ONELINE, "Name of the home planet"))

    def set(self, field_id, value):
        """
        setter method to assign attribute
        """
        self.field_id=value

    def get(self, field_id):
        """
        getter method to return attribute value
        """
        return self.field_id

    def get_list_fields(self):
        """
        returns list of ordered fields/attributes associated to the model
        """
        return self.fields
