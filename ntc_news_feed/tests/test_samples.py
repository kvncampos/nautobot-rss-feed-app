import pytest


def test_numbers():
    assert 1 + 1 == 2
    assert 2 * 2 == 4
    assert 10 / 2 == 5


def test_letters():
    assert "a" == "a"
    assert "abc".upper() == "ABC"
    assert "hello world".split() == ["hello", "world"]


def test_bool():
    assert True is True
    assert False is not True
    assert bool(1) is True
