from .. import console, fields
from ..exceptions import ConsoleError
import pytest

def custom_mirror_input(field):
    return field

console.raw_input=custom_mirror_input

def test_prompt():
    field=fields.Field("test_field", "test field", fields.Field.TYPE_TEXT_ONELINE, "this is a test field")
    assert console.prompt(field).startswith("test field")==True

def test_input_parser():
    sys_args=['-f', 'myfile']
    exts=["test"]
    models=["test_model"]
    assert console.input_parser(models, exts, sys_args)==["test_model","myfile","test"]
    with pytest.raises(ConsoleError):
        console.input_parser("", "", sys_args)
