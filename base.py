class Base:

    def __init__(self, inner = None):
        self.value = None
        self.derivative = None
        self.inner = inner

    def __add__(self, other):
        return Sum(self, other)

    def __radd__(self, other):
        return Sum(self, other)

    def __evaluate__(self, x):
        if isinstance(self.inner, Base):
            self.inner.df(x)
            self.__calculate_value_and_derivative__(x)
        else:
            self.value = self.inner
            self.derivative = 0

    def __calculate_value_and_derivative__(self, x):
        pass

    def df(self, x):
        self.__evaluate__(x)
        return self.derivative

class Arithmetic(Base):

    def __evaluate__(self, x):
        self.__calculate_value_and_derivative__(x)


class Sum(Arithmetic):

    def __init__(self, summand1, summand2):
        self.summand1 = summand1
        self.summand2 = summand2

    def __calculate_value_and_derivative__(self, x):
        if isinstance(self.summand1, Base):
            self.summand1.df(x)
        if isinstance(self.summand2, Base):
            self.summand2.df(x)

        if isinstance(self.summand1, Base) and isinstance(self.summand2, Base):
            self.value = self.summand1.value + self.summand2.value
            self.derivative = self.summand1.derivative + self.summand2.derivative
        elif isinstance(self.summand1, Base):
            self.value = self.summand1.value + self.summand2
            self.derivative = self.summand1.derivative
        elif isinstance(self.summand2, Base):
            self.value = self.summand1 + self.summand2.value
            self.derivative = self.summand2.derivative