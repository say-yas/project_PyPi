import numpy as np
import matplotlib.pyplot as plt
from src.FixedPrecision import FixedPrecision
from src.FloatNumber import FloatNumber
from src.RationalNumber import RationalNumber
from decimal import Decimal, getcontext, InvalidOperation

class PolygonApproximation:
    def __init__(self, sides):
        if isinstance(sides, int):
            self.sides = sides
        elif isinstance(sides, (FixedPrecision, FloatNumber, RationalNumber)):
            self.sides = int(sides.value)
        else:
            raise TypeError("Number of sides must be an integer, FixedPrecision, FloatNumber, or RationalNumber instance")
        
        if self.sides < 3:
            raise ValueError("Number of sides must be greater than or equal to 3")

        self.approximations = []

    def approximate_pi_with_polygon(self, typeoutput="FixedPrecision", outputprec=6):
        try:
            if typeoutput == "Decimal":
                getcontext().prec = outputprec
                side_length = 2 * Decimal(np.sin(np.pi / self.sides))
                perimeter = Decimal(self.sides) * side_length
                approx_pi = perimeter / 2
                return approx_pi
            else:
                side_length = 2 * np.sin(np.pi / self.sides)
                perimeter = self.sides * side_length
                approx_pi = perimeter / 2
                if typeoutput == "FixedPrecision":
                    return FixedPrecision(approx_pi, outputprec)
                elif typeoutput == "FloatNumber":
                    return FloatNumber(approx_pi)
                else:
                    return float(approx_pi)
        except (OverflowError, InvalidOperation) as e:
            print(f"An error occurred while approximating π with a polygon of {self.sides} sides: {e}")
            return None

    def calculate_approximations(self, precision, fixed_values=None):
        try:
            if isinstance(precision, (FixedPrecision, FloatNumber, RationalNumber)):
                precision = float(precision.value)
            elif not isinstance(precision, (int, float)) or precision <= 0:
                raise ValueError("Precision must be a positive number")

            if fixed_values:
                for sides in fixed_values['sides']:
                    self.sides = sides
                    approx_pi = self.approximate_pi_with_polygon(typeoutput="FixedPrecision")
                    if approx_pi is not None:
                        self.approximations.append((sides, float(approx_pi.value)))
            else:
                current_approximation = float(self.approximate_pi_with_polygon(typeoutput="FixedPrecision").value)
                self.approximations.append((self.sides, current_approximation))
            
                while abs(current_approximation - np.pi) > precision:
                    self.sides *= 2
                    current_approximation = float(self.approximate_pi_with_polygon(typeoutput="FixedPrecision").value)
                    self.approximations.append((self.sides, current_approximation))
        except Exception as e:
            print(f"An error occurred during the calculation of approximations: {e}")

