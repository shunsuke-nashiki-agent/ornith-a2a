"""mathlib — 小さなユーティリティ。issue → 自律エージェントが機能を足していく土台。"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def base_convert(n, base):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError('base_convert(n, base) requires an int for n')
    if not isinstance(base, int) or isinstance(base, bool):
        raise TypeError('base_convert(n, base) requires an int for base')
    if not 2 <= base <= 36:
        raise ValueError('base_convert(n, base) requires 2 <= base <= 36')

    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if n == 0:
        return '0'

    negative = n < 0
    n = abs(n)
    chars = []
    while n > 0:
        n, remainder = divmod(n, base)
        chars.append(digits[remainder])
    chars.reverse()
    text = ''.join(chars)
    return '-' + text if negative else text


def roman(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError('roman(n) requires an int')
    if not 1 <= n <= 3999:
        raise ValueError('roman(n) requires 1 <= n <= 3999')

    table = (
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
    )

    parts = []
    for value, symbol in table:
        count, n = divmod(n, value)
        parts.append(symbol * count)
    return ''.join(parts)
