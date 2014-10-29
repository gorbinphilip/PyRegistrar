from .. import fields

def test_fields():
    field=fields.Field("test_field", "test field", fields.Field.TYPE_NONE, "this is a test field")
    assert isinstance(field, fields.Field)==True
    assert field.field_id=="test_field"
    assert field.field_name=="test field"
    assert field.field_type=="none"
    assert field.field_description=="this is a test field"
