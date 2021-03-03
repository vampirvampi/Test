import pytest


def len_is_odd(str):
    try:
        return (len(str) % 2 == 0)
    except TypeError:
        return False


class Teststr:
    def test_1(self):
        assert len_is_odd("") == True

    def test_2(self):
        assert len_is_odd("1111") == True

    @pytest.mark.parametrize("x", [''])
    def test_3(self,x):
        assert len_is_odd(x) == True
