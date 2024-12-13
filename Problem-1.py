class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation

    def calculate(self):
        if self.operation == "+" :
            return self.a + self.b
        elif self.operation == "-":
            return self.a - self.b
        elif self.operation == "*":
            return self.a * self.b
        elif self.operation == "/":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Division by zero is not allowed"
        else:
            return "Invalid operator"

a = input("Enter the value of a ")
b = input("Enter the value of b ")
operation = input("Enter the operator ")

calculator = Calculator(a, b, operation)
result = calculator.calculate()
print("result is: ",result)
