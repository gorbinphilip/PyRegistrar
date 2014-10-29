from  ..extensions import plain
import os

def test_plain():
    p=plain.Export()
    file="/tmp/test454654.txt"
    data=[("name","me"), ("age","0")]
    p.export(data, file)
    f=open(file)
    data=f.read()
    assert data.__contains__("name")
    os.remove(file)
