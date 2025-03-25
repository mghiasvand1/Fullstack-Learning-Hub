class Calculator:

    def sum(self, a, b):
        print(f"{a} + {b} : {a + b}")

    def subtract(self, a, b):
        print(f"{a} - {b} : {a - b}")

    def multiply(self, a, b):
        print(f"{a} * {b} : {a * b}")

    def division(self, a, b):
        print(f"{a} / {b} : {a / b}")


myCalc = Calculator()

myCalc.sum(20,5)
myCalc.subtract(20,5)
myCalc.multiply(20,5)
myCalc.division(20,5)