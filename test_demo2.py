import pytest

# @pytest.mark.skip
def test_firstProgram():
    msg="Hello"
    assert msg== "Hi","Test failed"


# @pytest.mark.xfail

def test_secondCreditCard():
    a=4
    b=6
    assert a+2==6,"Addition do not match"

