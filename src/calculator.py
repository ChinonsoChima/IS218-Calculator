from src.model.calculation import Calculation
from src.operations.add import add
from src.operations.subtract import subtract
from src.operations.multiply import multiply
from src.operations.divide import divide
from src.operations.power import power
from src.operations.root import root


class Calculator:
    calculation = []

    def sum(self, a, b):
        calculation = Calculation(a, b, add)
        Calculator.calculation.append(calculation)
        return calculation.getResult()

    def subtract(self, a, b):
        calculation = Calculation(a, b, subtract)
        Calculator.calculation.append(calculation)
        return calculation.getResult()

    def multiply(self, a, b):
        calculation = Calculation(a, b, multiply)
        Calculator.calculation.append(calculation)
        return calculation.getResult()

    def divide(self, a, b):
        calculation = Calculation(a, b, divide)
        Calculator.calculation.append(calculation)
        return calculation.getResult()

    def power(self, a, b):
        calculation = Calculation(a, b, power)
        Calculator.calculation.append(calculation)
        return calculation.getResult()

    def root(self, a, b):
        calculation = Calculation(a, b, root)
        Calculator.calculation.append(calculation)
        return calculation.getResult()