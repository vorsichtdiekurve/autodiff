class Variable:
    def __init__(self):
        self.tangent = None
        self.primal = None

    def __add__(self, other):
        return Differentiable()

    def __mul__(self, other):
        return Differentiable()

    def __truediv__(self, other):
        return Differentiable()

    def df(self, x):
        self.primal = x
        self.tangent = 1