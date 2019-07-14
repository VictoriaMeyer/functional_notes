"""A simple closure
"""


def outer(outer_arg):
    """
    A "function factory"
    """
    def inner(inner_arg):
        """Produced function
        """
        return inner_arg + outer_arg
    return inner
