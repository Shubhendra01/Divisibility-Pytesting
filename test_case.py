import Divisibility
import pytest

@pytest.mark.parametrize("num,output",[(5,True),(2,False),(10,True),(7, False)])
def test_divby5(num, output):
    result = Divisibility.divby5(num)
    assert result == output

@pytest.mark.parametrize("num2,output2",[(14,True),(15,False),(21,True),(12, False)])
def test_divby7(num2, output2):
    result = Divisibility.divby7(num2)
    assert result == output2

@pytest.mark.parametrize("num3,output3",[(45,True),(13,False)])
def test_divby9(num3, output3):
    result = Divisibility.divby9(num3)
    assert result == output3

@pytest.mark.parametrize("num4,output4",[(121,True),(34,False)])
def test_divby11(num4, output4):
    result = Divisibility.divby11(num4)
    assert result == output4
