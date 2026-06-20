class BasicCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2
    def subtraction(self):
        return self.num1 - self.num2
    def multiplication(self):
        return self.num1 * self.num2
    def division(self):
        if self.num2 == 0:
            return "Cannot divide by 0"
        return self.num1 / self.num2

calc = BasicCalculator(8, 2)

print(f"Addition: {calc.num1} + {calc.num2} = {calc.addition()}")
print(f"Subtraction: {calc.num1} - {calc.num2} = {calc.subtraction()}")
print(f"Multiplication: {calc.num1} * {calc.num2} = {calc.multiplication()}")
print(f"Division: {calc.num1} / {calc.num2} = {calc.division()}")
