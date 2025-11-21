class Calculator:

    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op

    def calculate(self):

        if self.op == "add":
            x = self.a + self.b

        elif self.op == "subtract":
            x = self.a - self.b

        elif self.op == "multiply":
            x = self.a * self.b

        elif self.op == "divide":
            if self.b == 0:
                x = "division error"
            else:
                x = self.a / self.b

        else:
            x = "invalid op"

        return x


a = float(input("Enter first number : "))
b = float(input("Enter second number : "))
op = input("Enter operation (add/subtract/multiply/divide) : ")

calc = Calculator(a, b, op)
print(calc.calculate())
