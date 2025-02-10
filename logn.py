import math

from base import Base

class Logn(Base):

    def __calculate_value_and_derivative__(self, x):
        self.value = math.log(self.inner.value)
        self.derivative = self.inner.derivative / self.inner.value