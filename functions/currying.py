"""Currying with Python
"""

def func(x, y):
    """Simple function, called with two arguments
    """
    return x + y

def func_curry(x):
    """Function, called with first argument
    """
    def inner(y):
        """Function, called with second argument
        """
        return x + y
    return inner
