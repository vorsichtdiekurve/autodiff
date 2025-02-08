from variable import Variable

class X(Variable):
    def df(self, x):
        self.derivative = 1
        self.value = x
        return self.derivative