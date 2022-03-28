import Divisibility

def test_divby5():
    a = 10
    result = Divisibility.divby5(a)
    assert result == True
def test_divby5_1():
    a = 11
    result = Divisibility.divby5(a)
    assert result == False

def test_divby7():
    a = 14
    result = Divisibility.divby7(a)
    assert result == True
def test_divby7_1():
    a = 15
    result = Divisibility.divby7(a)
    assert result == False

def test_divby9():
    a = 27
    result = Divisibility.divby9(a)
    assert result == True
def test_divby9_1():
    a = 17
    result = Divisibility.divby9(a)
    assert result == False

def test_divby11():
    a = 11
    result = Divisibility.divby11(a)
    assert result == True
def test_divby11_1():
    a = 18
    result = Divisibility.divby11(a)
    assert result == False