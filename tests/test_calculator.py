from calculator import add, subtract

def test_add():
    assert add(3, 2) == 5

def test_subtract():
    assert subtract(7, 4) == 3
