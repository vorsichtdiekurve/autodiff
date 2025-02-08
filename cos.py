from variable import Variable
from math import sin, cos

class Cos(Variable):
    def df(self, x):
        self.inner.df(x)
        self.value = cos(self.inner.value)
        self.derivative = -sin(self.inner.value) * self.inner.derivative
        return self.derivative