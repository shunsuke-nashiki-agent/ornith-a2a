import pytest

from mathlib import add, multiply, roman, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0


@pytest.mark.parametrize('value, expected', [
    (1, 'I'),
    (3, 'III'),
    (4, 'IV'),
    (9, 'IX'),
    (14, 'XIV'),
    (40, 'XL'),
    (90, 'XC'),
    (400, 'CD'),
    (900, 'CM'),
    (1994, 'MCMXCIV'),
    (3999, 'MMMCMXCIX'),
])
def test_roman(value, expected):
    assert roman(value) == expected


@pytest.mark.parametrize('value', [0, 4000, -1])
def test_roman_out_of_range(value):
    with pytest.raises(ValueError):
        roman(value)


@pytest.mark.parametrize('value', [1.5, 'X', None, True, False])
def test_roman_rejects_non_int(value):
    with pytest.raises(TypeError):
        roman(value)
