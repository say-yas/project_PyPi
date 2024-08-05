import random
from src.FixedPrecision import FixedPrecision
from src.FloatNumber import FloatNumber
from src.RationalNumber import RationalNumber
from decimal import Decimal

class MonteCarloApproximation:
    def __init__(self, num_points):
        if isinstance(num_points, int):
            self.num_points = num_points
        elif isinstance(num_points, (FixedPrecision, FloatNumber, RationalNumber)):
            self.num_points = int(num_points.value)
        else:
            raise TypeError("Number of points must be an integer, FixedPrecision, FloatNumber, or RationalNumber instance")

    def calculate_approximation(self, typeoutput="FixedPrecision", outputprec=6):
        """
        Approximates pi using the Monte Carlo method with the specified number of random points.
        Returns the approximation in the specified output type with the desired precision.
        """
        try:
            if self.num_points <= 0:
                raise ValueError("Number of points must be a positive integer")

            points_inside_circle = 0
            for _ in range(self.num_points):
                x = random.uniform(-1, 1)
                y = random.uniform(-1, 1)
                if x**2 + y**2 <= 1:
                    points_inside_circle += 1

            approx_pi = 4 * points_inside_circle / self.num_points

            if typeoutput == "FixedPrecision":
                return FixedPrecision(approx_pi, outputprec)
            elif typeoutput == "FloatNumber":
                return FloatNumber(approx_pi)
            elif typeoutput == "Decimal":
                return Decimal( Decimal(approx_pi).quantize(Decimal(1)/(10**Decimal(outputprec)) ))
            else:
                return float(approx_pi)
        except Exception as e:
            print(f"Error: {e}")
            return None
