import numpy as np
from src.FixedPrecision import FixedPrecision
from src.FloatNumber import FloatNumber
from src.RationalNumber import RationalNumber
from decimal import Decimal

class PiCalculator:
    def __init__(self, num_digits):
        """
        Initialize the PiCalculator with the number of digits to compute π.
        :param num_digits: Number of digits, must be an integer or an instance of FixedPrecision, FloatNumber, or RationalNumber.
        """
        if isinstance(num_digits, int):
            self.num_digits = num_digits
        elif isinstance(num_digits, (FixedPrecision, FloatNumber, RationalNumber)):
            self.num_digits = int(num_digits.value)
        else:
            raise TypeError("Number of digits must be an integer, FixedPrecision, FloatNumber, or RationalNumber instance")

        if self.num_digits <= 0:
            raise ValueError("Number of digits must be a positive integer")

    def compute_pi_gauss_legendre(self, typeoutput="FixedPrecision", outputprec=6):
        """
        Computes pi to the specified number of digits using the Gauss-Legendre algorithm.
        :param typeoutput: The type of output ("FixedPrecision", "FloatNumber", "Decimal", or "float").
        :param outputprec: The precision of the output when type is "FixedPrecision" or "Decimal".
        """
        try:

            if typeoutput == "FixedPrecision":
                a = FixedPrecision(1.0, outputprec) 
                b = FixedPrecision(1.0, outputprec) / FixedPrecision(np.sqrt(2), outputprec)
                t = FixedPrecision(1.0, outputprec) / FixedPrecision(4.0, outputprec)
                p = FixedPrecision(1.0, outputprec)
            elif typeoutput == "FloatNumber":
                a = FloatNumber(1.0) 
                b = FloatNumber(1.0) / FloatNumber(np.sqrt(2))
                t = FloatNumber(1.0) / FloatNumber(4.0)
                p = FloatNumber(1.0)
            elif typeoutput == "Decimal":
                a = Decimal(1.0)
                b = Decimal(1.0) / Decimal(np.sqrt(2))
                t = Decimal(1.0) / Decimal(4.0)
                p = Decimal(1.0)
            else:
                a = float(1.0)
                b = float(1.0) / float(np.sqrt(2))
                t = float(1.0) / float(4.0)
                p = float(1.0)


            for _ in range(self.num_digits):

                if typeoutput == "FixedPrecision":
                    a_next = (a + b) / FixedPrecision(2, outputprec)
                    a_next.decimal_places = outputprec
                    b = pow(a * b, 0.5)
                    b.decimal_places = outputprec
                    t = t - p * pow(a - a_next , 2)
                    t.decimal_places = outputprec
                    a = a_next
                    p = p * FixedPrecision(2, outputprec)   
                    p.decimal_places = outputprec
                elif typeoutput == "FloatNumber":
                    a_next = (a + b) / FloatNumber(2)
                    b = pow(a * b, 0.5)
                    t = t - p * pow(a - a_next , 2)
                    a = a_next
                    p = p * FloatNumber(2)
                elif typeoutput == "Decimal":
                    a_next = (a + b) / Decimal(2)
                    b = Decimal(np.sqrt(a * b))
                    t -= p * (a - a_next) ** 2
                    a = a_next
                    p *= Decimal(2)
                    
                else:
                    a_next = (a + b) / 2
                    b = np.sqrt(a * b)
                    t = t - p * (a - a_next) ** 2
                    a = a_next
                    p = p * 2

            if typeoutput == "FixedPrecision":
                pi = pow(a + b, 2) / (FixedPrecision(4, outputprec) * t)
                return FixedPrecision(pi.value, outputprec) 
            elif typeoutput == "FloatNumber":
                pi = pow(a + b, 2) / (4 * t)
                return pi
            elif typeoutput == "Decimal":
                pi = (a + b) ** 2 / (Decimal(4) * t)
                return Decimal( Decimal(pi).quantize(Decimal(1)/(10**Decimal(outputprec)) ))
            else:
                return float((a + b) ** 2 / (4 * t))
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

    def compute_pi_nilakantha(self, typeoutput="FixedPrecision", outputprec=6):
        """
        Computes pi to the specified number of digits using the Nilakantha series.
        :param typeoutput: The type of output ("FixedPrecision", "FloatNumber", "Decimal", or "float").
        :param outputprec: The precision of the output when type is "FixedPrecision" or "Decimal".
        """
        try:
            if typeoutput == "FixedPrecision":
                pi = FixedPrecision(3.0, outputprec) 
                sign = FixedPrecision(-1.0, outputprec)
            elif typeoutput == "FloatNumber":
                pi = FloatNumber(3.0) 
                sign = FloatNumber(-1.0)
            elif typeoutput == "Decimal":
                pi = Decimal(3.0)
                sign = Decimal(-1.0)
            else:
                pi = float(3.0)
                sign = float(-1.0)

            for k in range(2, self.num_digits * 2, 2):

                if typeoutput == "FixedPrecision":
                    sign = sign * FixedPrecision(-1.0, outputprec)
                    deno = FixedPrecision(k * (k + 1) * (k + 2), outputprec)
                    term = FixedPrecision(4.0, outputprec) / deno
                elif typeoutput == "FloatNumber":
                    sign = sign * FloatNumber(-1.0)
                    deno = FloatNumber(k * (k + 1) * (k + 2))
                    term = FloatNumber(4.0) / deno 
                elif typeoutput == "Decimal":
                    sign = sign * Decimal(-1.0)
                    deno = Decimal(k) * Decimal(k + 1) * Decimal(k + 2) 
                    val = Decimal(4.0)/ deno
                    term = Decimal( Decimal( val ).quantize(Decimal(1)/(10**Decimal(outputprec)) ))
                else:
                    sign = sign * float(-1.0)
                    term = 4 / (k * (k + 1) * (k + 2))

                pi = pi + sign * term

            if typeoutput == "FixedPrecision":
                return FixedPrecision(pi.value, outputprec) 
            elif typeoutput == "FloatNumber":
                return pi
            elif typeoutput == "Decimal":
                return Decimal( Decimal(pi).quantize(Decimal(1)/(10**Decimal(outputprec)) ))
            else:
                return float(pi)
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
