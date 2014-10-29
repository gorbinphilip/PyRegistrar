from .. import registrar
import os, random, shutil

def test_register():
    registrar.register("Alien", "/tmp/test", "plain")
    assert os.path.exists("/tmp/test")==True
    os.remove("/tmp/test")

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
