import pytest

@pytest.mark.usefixtures("setup")
class Test:
    def test_main(self):
        print("I will be second because of fixture")
    def test_main1(self):
        print("I will be third because of fixture")
    def test_main2(self):
        print("I will be fourth because of fixture")
    def test_main3(self):
        print("I will be fifth because of fixture")




