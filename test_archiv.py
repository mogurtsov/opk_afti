assert __name__ == '__main__'

import archiv

def test_dict():
    for i in [{"1":1,"2":2},{'1':"1",'2':"2"}]:
        assert archiv.decompress(archiv.compress(i))==i
    return True

def test_list():
    for i in [[1,2],["1","2"]]:
        assert archiv.decompress(archiv.compress(i))==i
    return True

def test_empty_dict():
    assert archiv.decompress(archiv.compress({}))=={}
    return True

def test_empty_list():
    assert archiv.decompress(archiv.compress([]))==[]
    return True

tests=[test_dict,test_list,test_empty_dict,test_empty_list]
for f in tests:
    print(f())
