import pytest


def sqr(x):
    return x * x


class TestInt:
    def test_1(self):
        assert sqr(1) == 1

    def test_2(self):
        assert sqr(-1) == 1

    @pytest.mark.parametrize("X", [0, 1])
    def test_3(self, X):
        assert sqr(X) == X
