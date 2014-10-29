from ..models import Model, Alien
from ..fields import Field
import pytest

def test_Model():
    with pytest.raises(NotImplementedError):
        tmp=Model()

def test_Alien():
    tmp=Alien()
    assert isinstance(tmp, Alien)==True
    assert type(tmp.get_list_fields())==list
    for field in tmp.fields:
        assert isinstance(field, Field)
    for field in tmp.fields:
        tmp.set(field.field_id, "test value")
        assert tmp.get(field.field_id)=="test value"
