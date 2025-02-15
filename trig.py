from base import Base
from math import cos, sin, tan

class Sin(Base):

    def __calculate_value_and_derivative__(self, x):
        self.value = sin(self.inner.value)
        self.derivative = cos(self.inner.value) * self.inner.derivative

    def __calculate_constant__(self):
        self.value = sin(self.inner)

class Cos(Base):

    def __calculate_value_and_derivative__(self, x):
        self.value = cos(self.inner.value)
        self.derivative = -sin(self.inner.value) * self.inner.derivative

    def __calculate_constant__(self):
        self.value = cos(self.inner)

class Tan(Base):

    def __calculate_value_and_derivative__(self, x):
        self.value = tan(self.inner.value)
        self.derivative = self.inner.derivative / (cos(self.inner.value)**2)

    def __calculate_constant__(self):
        self.value = tan(self.inner)

class Cotan(Base):

    def __calculate_value_and_derivative__(self, x):
        self.value = 1 / tan(self.inner.value)
        self.derivative = -self.inner.derivative / (sin(self.inner.value)**2)

    def __calculate_constant__(self):
        self.value = 1 / tan(self.inner)