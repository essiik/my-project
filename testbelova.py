def name_1(x):
    l = x.split()
    print((l))
    if len(l) == 1:
        return l
    return l

def test_one():
    assert "l" in ''.join (name_1('Hello world'))
def test_two():
    assert len(name_1('fhrksn')) == 1
def test_three():
    assert "goodbye" in name_1('dear fiend goodbye')
def test_four():
    assert len(name_1('')) == 0
def test_fine():
    assert isinstance(name_1('some text'), list)