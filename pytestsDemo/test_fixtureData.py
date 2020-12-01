import pytest
from pytestsDemo.Baseclass import Baseclass
@pytest.mark.usefixtures("dataload")

class Testexample(Baseclass):

    def test_editprofile(self,dataload):
        log = self.getLogger()
        log.info(dataload[0])
        log.info(dataload[1])
        print(dataload[1])
