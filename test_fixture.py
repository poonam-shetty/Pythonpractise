
import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

 def test_fixtureDemo(self):
    print("I will be execute steps in fixturDemo method")


 def test_fixtureDemo1(self):
    print("I will be execute steps in fixturDemo1 method")

 def test_fixtureDemo2(self):
    print("I will be execute steps in fixturDemo2 method")

 def test_fixtureDemo3(self):
    print("I will be execute steps in fixturDemo3 method")

 def test_fixtureDemo4(self):
    print("I will be execute steps in fixturDemo4 method")


