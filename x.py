from base import Base

class X(Base):

    def __evaluate__(self, x):
        self.derivative = 1
        self.value = x