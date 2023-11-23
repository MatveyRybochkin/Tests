class FactorialCalculator:
    def calculate_factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calculate_factorial(n - 1)

calculator = FactorialCalculator()
factorial = calculator.calculate_factorial(0)
print(factorial)
