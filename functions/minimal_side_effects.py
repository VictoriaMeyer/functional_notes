# pylint: disable=too-few-public-methods

"""Minimizing side effects in classes
"""


class InitOnly:
    """Example for init-only definitions.
    """
    def __init__(self, count):
        self.attr1 = self._make_attr(count)
        self.attr2 = self._make_attr(count + 10)

    @staticmethod
    def _make_attr(count):
        """Do many things to create an attribute.
        """
        attr = []
        for x in range(count):
            # do something actual useful here
            attr.append(x)
        return tuple(attr)
