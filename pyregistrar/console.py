from .fields import Field
import argparse
import random


def prompt(field):
    """method to prompt and return user input.
    :param :field instance of registrar.Field"""
    input_data=raw_input(field.field_name+" :-> ")
    if field.field_type==Field.TYPE_NONE:
        pass
    else:
        return input_data


def main(models, extensions, args):
    parser=argparse.ArgumentParser()
    parser.add_argument("-m", "--model", default=models[0], help="select model required to register", choices=models)
    parser.add_argument("-f", "--file", default=str(random.randrange(9999)), help="set output file name")
    parser.add_argument("-e", "--extension", default=extensions[0], help="select output file format", choices=extensions)
    ret=parser.parse_args(args)
    return [ret.model, ret.file, ret.extension]
