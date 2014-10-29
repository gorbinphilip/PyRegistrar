from  ..extensions import pdf
import os

def test_plain():
    p=pdf.Export()
    file="/tmp/tst.txt"
    data=[("name","me"), ("age","0")]
    p.export(data, file)
    assert os.path.exists(file)==True
    os.remove(file)
