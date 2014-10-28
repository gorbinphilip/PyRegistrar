from .. import registrar

def test_fields():
    field=registrar.Field("test_field", "test field", registrar.Field.TYPE_NONE, "this is a test field")
    assert isinstance(field, registrar.Field)==True
    assert field.field_id=="test_field"
    assert field.field_name=="test field"
    assert field.field_type=="none"
    assert field.field_description=="this is a test field"

def test_register():
    pass

def test_get_models():
    models=registrar.get_models()
    assert type(models)==list

def test_get_extensions():
    pass
