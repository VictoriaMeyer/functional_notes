"""Simple example using Freezer
"""

from funtions.freezing import Freezer


class Old:
    """Existing class to frozen
    """
    def __init__(self, value):
        self.value = value

    def meth(self, factor):
        """Do something
        """
        return self.value * factor


class OldFrozen(Old, Freezer):
    """Old class but frozen
    """
    def __init__(self, *args, **kwargs):
        Freezer.__init__(self)
        super().__init__(*args, **kwargs)
        self._frozen = True


def test():
    """Test the freezing
    """
    old_frozen = OldFrozen(10)
    print(old_frozen.meth(3))
    # should raise an exception
    old_frozen.value = 12
