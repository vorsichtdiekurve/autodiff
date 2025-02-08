from base import Base
from math import sin, cos

class Cos(Base):

    def __evaluate__(self, x):
        self.inner.df(x)
        self.value = cos(self.inner.value)
        self.derivative = -sin(self.inner.value) * self.inner.derivative