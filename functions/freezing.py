"""
Instance freezer
"""


class Freezer:
    """
    Simple helper class to prevent changing of attributes on instances
    """
    def __init__(self):
        self._frozen = False

    def __setattr__(self, name, value):
        if name != '_frozen' and self._frozen:
            raise AttributeError(f'Cannot set attribute {name}')
        super().__setattr__(name, value)

    def freeze(self):
        """Turn of freezing
        """
        self._frozen = True

    def unfreeze(self):
        """Turn off freezing
        """
        self._frozen = False
