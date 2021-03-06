from .fields import Field
from .exceptions import ConsoleError
import argparse
import random


def prompt(field):
    """
    method to prompt and return user input.
    :field instance of registrar.Field
    """
    try:
        if field.field_type==Field.TYPE_NONE:
            print field.field_name
            return
        else:
            input_data=raw_input(field.field_name+" :-> ")
            if field.field_type==Field.TYPE_NUMBER:
                try:
                    float(input_data)
                    return input_data
                except ValueError:
                    print "Invalid input..Retry"
                    return prompt(field)
            else:
                return input_data
    except Exception:
        raise ConsoleError("unable to prompt user")


def input_parser(models, extensions, args):
    """
    parser for args based on available models and extensions
    :models list of available models
    :extensions list of available extensions
    returns resolved model, file, extension list
    """
    try:
        parser=argparse.ArgumentParser()
        parser.add_argument("-m", "--model", default=models[0], help="select model required to register", choices=models)
        parser.add_argument("-f", "--file", default=str(random.randrange(9999)), help="set output file name")
        parser.add_argument("-e", "--extension", default=extensions[0], help="select output file format", choices=extensions)
        ret=parser.parse_args(args)
        return [ret.model, ret.file, ret.extension]
    except Exception:
        raise ConsoleError("unable to parse data")
