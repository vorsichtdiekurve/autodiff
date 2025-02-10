from base import Base
from invalid_argument_error import InvalidArgumentError


class X(Base):

    def __init__(self, inner=None):
        if inner is not None:
            raise InvalidArgumentError("X denotes the variable and cannot have an inner value")
        super().__init__(inner)

    def __evaluate__(self, x):
        self.derivative = 1
        self.value = x