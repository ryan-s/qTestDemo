import pytest

@pytest.mark.skip
def test_skip():
    pass


class TestClass(object):

    def test_class_1(self):
        assert 5 == 8