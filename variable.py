class Variable:

    def __init__(self, inner: 'Variable' = None):
        self.value = None
        self.derivative = None
        self.inner = inner

    def __add__(self, other):
        return ()

    def df(self, x):
        pass