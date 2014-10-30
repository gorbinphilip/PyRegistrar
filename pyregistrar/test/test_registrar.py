from .. import registrar,console
from ..exceptions import ExtensionError, ModelError, RegistrarError
from . import mock
import os, random, shutil, pytest

console.raw_input=mock.raw_input

def test_register():
    registrar.register("Alien", "/tmp/test9999", "plain")
    assert os.path.exists("/tmp/test9999")==True
    os.remove("/tmp/test9999")
    with pytest.raises(RegistrarError):
        registrar.register("test","/tmp/ddf","plain")

def test_find_modules():
    test_dir="/tmp/"+str(random.randrange(999))
    os.makedirs(test_dir)
    for i in range(1,5):
        f=open(test_dir+"/"+str(i)+".py", "w")
        f.close()
    f_new=open(test_dir+"/"+"__init__.py", "w")
    f_new.close()
    modules=registrar.find_modules(test_dir)
    shutil.rmtree(test_dir)
    assert "__init__.py" not in modules
    assert len(modules)==4

def test_get_models():
    models=registrar.get_models()
    assert type(models)==list

def test_get_extensions():
    extensions=registrar.get_extensions()
    assert type(extensions)==list

def test_load_class():
    with pytest.raises(ExtensionError):
        registrar.load_class("fail","fail","fail")

def test_main():
    ret=registrar.main(["-f","/tmp/343545456"])
    assert ret=="/tmp/343545456"
    try:
        os.remove("/tmp/343545456")
    except Exception:
        pass
    assert type(registrar.main(["-f","/fail"]))==ExtensionError

