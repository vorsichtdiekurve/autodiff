from base import Base
from math import sin, cos

class Cos(Base):

    def __calculate_value_and_derivative__(self, x):
        self.value = cos(self.inner.value)
        self.derivative = -sin(self.inner.value) * self.inner.derivative