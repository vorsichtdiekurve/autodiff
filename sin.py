from base import Base
from math import cos, sin

class Sin(Base):

    def __evaluate__(self, x):
        self.inner.df(x)
        self.value = sin(self.inner.value)
        self.derivative = cos(self.inner.value) * self.inner.derivative