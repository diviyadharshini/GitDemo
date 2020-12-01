import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    msg = "Hello"
    assert msg =="Hi","Test Case failed not matched"
@pytest.mark.xfail
def test_seconddiviya():
    a=5
    b=6
    assert a+1 == 6, "No match"