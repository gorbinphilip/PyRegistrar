from .. import console, registrar

def custom_mirror_input(field):
    return field

console.raw_input=custom_mirror_input

def test_prompt():
    field=registrar.Field("test_field", "test field", registrar.Field.TYPE_TEXT_ONELINE, "this is a test field")
    assert console.prompt(field).startswith("test field")==True

