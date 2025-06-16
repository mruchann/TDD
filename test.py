import unittest
from calculator import *
from scientific_calculator import *

class CalculatorTests(unittest.TestCase):

    def test_calculator_available(self):
        calculator = Calculator()
        assert calculator is not None

    def test_scientific_calculator_available(self):
        scientific_calculator = ScientificCalculator()
        assert scientific_calculator is not None


    def test_add(self):
        calculator = Calculator()
        a, b = 1, 2
        assert calculator.add(a, b) == a + b

    def test_subtraction(self):
        calculator = Calculator()
        a, b = 1, 2
        assert calculator.subtract(a, b) == a - b


    def test_scientific_calculator_a_calculator(self):
        scientific_calculator = ScientificCalculator()
        assert isinstance(scientific_calculator, Calculator)

    def test_sin(self):
        scientific_calculator = ScientificCalculator()
        assert scientific_calculator.sin(0) == 0

    def test_cos(self):
        scientific_calculator = ScientificCalculator()
        assert scientific_calculator.cos(0) == 1

