import pytest
from Baseclass import Baseclass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(Baseclass):
    def test_editProfile(self,dataLoad):
        log= self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[2])


