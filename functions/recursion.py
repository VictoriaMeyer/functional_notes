"""Recursion speed in Python
"""


def loop(n):
    """Loop approach
    """
    res = 0
    for _ in range(n):
        res += 1
    return res


def recurse(n, res=0):
    """Recursion approach
    """
    if n > 0:
        res = recurse(n - 1, res + 1)
    return res
