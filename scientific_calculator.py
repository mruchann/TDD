from calculator import Calculator
import math

class ScientificCalculator(Calculator):
    def sin(self, x):
        return math.sin(x)

    def cos(self, x):
        return math.cos(x)