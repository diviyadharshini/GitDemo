import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

def test_Greetdiviya():
    print("Good Morning")


def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])