class A:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __repr__(self):
        return f'A({self.value1}, {self.value2})'