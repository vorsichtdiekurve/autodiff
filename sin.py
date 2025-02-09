from base import Base
from math import cos, sin

class Sin(Base):

    def __calculate_value_and_derivative__(self, x):
        self.value = sin(self.inner.value)
        self.derivative = cos(self.inner.value) * self.inner.derivative