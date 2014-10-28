from ..models import Model
import pytest

def test_model():
    with pytest.raises(NotImplementedError):
        tmp=Model()


