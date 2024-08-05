import numpy as np
from fractions import Fraction
from src.FixedPrecision import FixedPrecision
from src.FloatNumber import FloatNumber
from src.RationalNumber import RationalNumber
from decimal import Decimal

def continued_fraction_pi(numdigit=1, typeoutput="RationalNumber"):
    """
    Compute an approximation of pi using continued_fraction's formula.

    The formula is given by:
    pi = a0 + 1/(a1 + 1/(a2 + 1/(a3 + ...))) [continued fraction representation with (a_i)s from the digits list] 

    Args:
    numdigit: Number of digits to use for the approximation.
    typeoutput: The type of output ("RationalNumber", "Fraction" or "float").
    output: approximation of pi with certain number of digits.

    Returns:
    est_pi: Approximation of pi with the specified precision and output type.
    """
    try:
        digits = np.array([	3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, 1,
                   84, 2, 1, 1, 15, 3, 13, 1, 4, 2, 6, 6, 99, 1, 2, 2, 6, 3, 5, 1, 1, 6,
                     8, 1, 7, 1, 2, 3, 7, 1, 2, 1, 1, 12, 1, 1, 1, 3, 1, 1, 8, 1, 1, 2, 1,
                       6, 1, 1, 5, 2, 2, 3, 1, 2, 4, 4, 16, 1, 161, 45, 1, 22, 1, 2, 2, 1,
                         4, 1, 2, 24, 1, 2, 1, 3, 1, 2, 1], dtype=int)
        
        if numdigit > len(digits):
            raise ValueError("The number of digits must be less than the length of the degits list=", len(digits))
        
        # for idx in range(int(numdigit)):
        # start from the bottom of the fraction [last digit]
        
        idx = int(numdigit) 
        if typeoutput == "Fraction":
            est_pi = Fraction(digits[idx])
        elif typeoutput == "RationalNumber":
            est_pi = RationalNumber(digits[idx])
        elif typeoutput == "FloatNumber":
            est_pi = FloatNumber(digits[idx])
        else:
            est_pi = digits[idx]

        # update using  a_i[current value] + 1 / a_(i+1)[previously computed fraction]
        for jdx in range(idx-1, -1, -1):
            if typeoutput == "Fraction":
                aj = Fraction(digits[jdx])
                tmp = Fraction(est_pi.denominator, est_pi.numerator)
            elif typeoutput == "RationalNumber":
                aj = RationalNumber(digits[jdx])
                tmp = RationalNumber(est_pi.denominator, est_pi.numerator)
            elif typeoutput == "FloatNumber":
                aj = FloatNumber(digits[jdx])
                tmp = FloatNumber(1.0) / est_pi
            else:
                aj = digits[jdx]
                tmp = 1 / est_pi
                
            est_pi = aj + tmp

            # Stop if too large
            if typeoutput == ["Fraction", "RationalNumber"]:
                if est_pi.numerator >= 2**64 or est_pi.denominator >= 2**64:
                    raise ValueError("The numerator or denominator is too large to be represented as a 64-bit integer.")
                    break

        pi_value = est_pi
        if typeoutput == "Fraction":
            return est_pi
        elif typeoutput == "RationalNumber":
            return est_pi
        elif typeoutput == "FloatNumber":
            return est_pi
        else:
            return pi_value
    except Exception as e:
        print(f"An error occurred while computing continued_fraction's pi: {e}")
        return None


