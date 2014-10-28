from .registrar import Field


def prompt(field):
    """method to prompt and return user input.
    :param :field instance of registrar.Field"""
    input_data=raw_input(field.field_name+" :-> ")
    if field.field_type==Field.TYPE_NONE:
        pass
    else:
        return input_data
