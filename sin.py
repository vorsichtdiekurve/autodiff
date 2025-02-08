from variable import Variable
from math import cos, sin

class Sin(Variable):
    def df(self, x):
        self.inner.df(x)
        self.value = sin(self.inner.value)
        self.derivative = cos(self.inner.value) * self.inner.derivative
        return self.derivative