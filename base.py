class Base:

    def __init__(self, inner = None):
        self.value = None
        self.derivative = None
        self.inner = inner

    def __add__(self, other):
        return Sum(self, other)

    def __radd__(self, other):
        return Sum(self, other)

    def __sub__(self, other):
        return Difference(self, other)

    def __rsub__(self, other):
        return Difference(other, self)

    def __mul__(self, other):
        return Product(self, other)

    def __rmul__(self, other):
        return Product(self, other)

    def __truediv__(self, other):
        return Quotient(self, other)

    def __rtruediv__(self, other):
        return Quotient(other, self)

    def __pow__(self, other):
        if isinstance(other, Base):
            return Exponential(self, other)
        else:
            return Power(self, other)

    def __rpow__(self, other):
        return Exponential(other, self)

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

class Difference(Arithmetic):

    def __init__(self, minuend, subtrahend):
        self.minuend = minuend
        self.subtrahend = subtrahend

    def __calculate_value_and_derivative__(self, x):
        if isinstance(self.minuend, Base):
            self.minuend.df(x)
        if isinstance(self.subtrahend, Base):
            self.subtrahend.df(x)

        if isinstance(self.minuend, Base) and isinstance(self.subtrahend, Base):
            self.value = self.minuend.value - self.subtrahend.value
            self.derivative = self.minuend.derivative - self.subtrahend.derivative
        elif isinstance(self.minuend, Base):
            self.value = self.minuend.value - self.subtrahend
            self.derivative = self.minuend.derivative
        elif isinstance(self.subtrahend, Base):
            self.value = self.minuend - self.subtrahend.value
            self.derivative = -self.subtrahend.derivative

class Product(Arithmetic):

    def __init__(self, factor1, factor2):
        self.factor1 = factor1
        self.factor2 = factor2

    def __calculate_value_and_derivative__(self, x):
        if isinstance(self.factor1, Base):
            self.factor1.df(x)
        if isinstance(self.factor2, Base):
            self.factor2.df(x)

        if isinstance(self.factor1, Base) and isinstance(self.factor2, Base):
            self.value = self.factor1.value * self.factor2.value
            self.derivative = self.factor1.derivative * self.factor2.value + self.factor1.value * self.factor2.derivative
        elif isinstance(self.factor1, Base):
            self.value = self.factor1.value * self.factor2
            self.derivative = self.factor1.derivative * self.factor2

class Quotient(Arithmetic):

    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    def __calculate_value_and_derivative__(self, x):
        if isinstance(self.dividend, Base):
            self.dividend.df(x)
        if isinstance(self.divisor, Base):
            self.divisor.df(x)
            if self.divisor.value == 0:
                raise ZeroDivisionError("Function is not differentiable at the point x={}.".format(x))
        elif self.divisor == 0:
            raise ZeroDivisionError("Function is not differentiable at the point x={}.".format(x))

        if isinstance(self.dividend, Base) and isinstance(self.divisor, Base):
            self.value = self.dividend.value / self.divisor.value
            self.derivative = (self.dividend.derivative * self.divisor.value - self.dividend.value * self.divisor.derivative) / self.divisor.value**2
        elif isinstance(self.dividend, Base):
            self.value = self.dividend.value / self.divisor
            self.derivative = self.dividend.derivative / self.divisor
        elif isinstance(self.divisor, Base):
            self.value = self.dividend / self.divisor.value
            self.derivative = -self.dividend * self.divisor.derivative / self.divisor.value**2

class Power(Arithmetic):

    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def __calculate_value_and_derivative__(self, x):
        self.base.df(x)

        self.value = self.base.value**self.exponent
        self.derivative = self.exponent * self.base.value**(self.exponent-1)

class Exponential(Arithmetic):

    def __init__(self, base, exponent):
        raise NotImplementedError
        self.base = base
        self.exponent = exponent

    def __calculate_value_and_derivative__(self, x):
        if isinstance(self.base, Base):
            self.base.df(x)

