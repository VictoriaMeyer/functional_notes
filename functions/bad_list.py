"""Bad list that modifies global state when not expected.
"""


GLOBAL_LIST = []

class BadList(list):
    """Bad list with "non-pure" behavior for `*`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0

    def __mul__(self, factor):
        """Multiplication with integer and with **SIDE EFFECT**.
        """
        GLOBAL_LIST.append(self.counter)
        self.counter += 1
        return super().__mul__(factor)
