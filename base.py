class Base:

    def __init__(self, inner: 'Base' = None):
        self.value = None
        self.derivative = None
        self.inner = inner

    def __evaluate__(self, x):
        pass

    def df(self, x):
        self.__evaluate__(x)
        return self.derivative