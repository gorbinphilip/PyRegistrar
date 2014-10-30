from .. import console, fields
from ..exceptions import ConsoleError
from . import mock
import pytest

console.raw_input=mock.raw_input

def test_prompt():
    field=fields.Field("test_field", "test field", fields.Field.TYPE_TEXT_ONELINE, "this is a test field")
    assert console.prompt(field)=="999"

def test_input_parser():
    sys_args=['-f', 'myfile']
    exts=["test"]
    models=["test_model"]
    assert console.input_parser(models, exts, sys_args)==["test_model","myfile","test"]
    with pytest.raises(ConsoleError):
        console.input_parser("", "", sys_args)

