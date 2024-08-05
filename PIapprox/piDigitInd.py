from decimal import Decimal
import decimal
from src.FixedPrecision import FixedPrecision
from src.FloatNumber import FloatNumber
from src.RationalNumber import RationalNumber

class PiCalculator:
    def __init__(self, precision):
        """
        Initialize the PiCalculator with the precision for computing π.
        :param precision: Precision, must be an integer, FixedPrecision, FloatNumber, or RationalNumber instance.
        """
        if isinstance(precision, (FixedPrecision, FloatNumber, RationalNumber)):
            self.precision = int(precision.value)
        elif isinstance(precision, int):
            self.precision = precision
        else:
            raise TypeError("Precision must be an integer, FixedPrecision, FloatNumber, or RationalNumber instance")
                
        if self.precision <= 0:
            raise ValueError("Precision must be a positive integer")
        
        self.context = decimal.getcontext()
        self.context.prec = self.precision + 1

    def recursive_pi_calc(self, start, end):
        """
        Recursive function to calculate intermediate values for the Chudnovsky algorithm.
        """
        try:
            if not all(isinstance(arg, int) for arg in [start, end]) or start < 0 or end <= start:
                raise ValueError("start and end must be non-negative integers with end > start")

            if end == start + 1:
                a = start
                P = -(6 * a - 5) * (2 * a - 1) * (6 * a - 1)
                Q = 10939058860032000 * a ** 3
                R = P * (545140134 * a + 13591409)
            else:
                mid = (start + end) // 2
                P_start_mid, Q_start_mid, R_start_mid = self.recursive_pi_calc(start, mid)
                P_mid_end, Q_mid_end, R_mid_end = self.recursive_pi_calc(mid, end)

                P = P_start_mid * P_mid_end
                Q = Q_start_mid * Q_mid_end
                R = Q_mid_end * R_start_mid + P_start_mid * R_mid_end

            return P, Q, R
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, None, None

    def compute_pi_digits(self, typeoutput="FixedPrecision", outputprec=6):
        """
        Computes the value of pi with the specified precision using the Chudnovsky algorithm.
        :param typeoutput: The type of output ("FixedPrecision", "FloatNumber", "Decimal", or "float").
        :param outputprec: The precision of the output when type is "FixedPrecision" or "Decimal".
        """
        try:
            P, Q, R = self.recursive_pi_calc(1, self.precision)
            pi_value = (426880 * decimal.Decimal(10005).sqrt() * Q) / (13591409 * Q + R)
            pi_value = +pi_value  # Apply the precision to pi

            if typeoutput == "FixedPrecision":
                return FixedPrecision(float(pi_value), outputprec)
            elif typeoutput == "FloatNumber":
                return FloatNumber(float(pi_value))
            elif typeoutput == "Decimal":
                return Decimal( Decimal(pi_value).quantize(Decimal(1)/(10**Decimal(outputprec)) ))
            else:
                return float(pi_value)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None




