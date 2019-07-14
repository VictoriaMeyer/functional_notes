"""Read data in `__init__()` and turn into immutable structure
"""

class Reader:
    """Read some data
    """
    def __init__(self, file_name):
        self.data = self._read(file_name)

    @staticmethod
    def _read(file_name):
        """Return tuple of tuple of read data.
        """
        data = []
        with open(file_name) as fobj:
            for line in fobj:
                data.append(tuple(line.split()))
        return tuple(data)


class ReaderOneLine:
    """Read some data
    """
    def __init__(self, file_name):
        self.data = self._read(file_name)

    @staticmethod
    def _read(file_name):
        """Return tuple of tuple of read data.
        """
        return tuple(tuple(line.split()) for line in open(file_name))
