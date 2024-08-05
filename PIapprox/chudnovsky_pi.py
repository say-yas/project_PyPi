import numpy as np
from src.FixedPrecision import FixedPrecision
from src.FloatNumber import FloatNumber
from src.RationalNumber import RationalNumber
from decimal import Decimal, getcontext
from PIapprox.factorial import factorial

def chudnovsky_pi(precision=None, typeoutput="FixedPrecision", outputprec=6, output=False):
    """
    Compute an approximation of pi using Chudnovsky's formula.

    The formula is given by:
    1/pi = (sqrt{10005}/4270934400)  *sum_k  (6k)! * (13591409 + 545140134k) / ((3k)! * (k!)^3 * (-640320)^(3k))

    Args:
    precision: The desired precision, an instance of FixedPrecision, FloatNumber, RationalNumber, int, or float.
    typeoutput: The type of output ("FixedPrecision", "FloatNumber", "Decimal", or "float").
    outputprec: The precision of the output when type is "FixedPrecision" or "Decimal".
    output: Whether to output the upper bound for the approximation.

    Returns:
    est_pi: Approximation of pi with the specified precision and output type.
    """
    
    try:
        
        if precision is not None:
            if isinstance(precision, (FixedPrecision, FloatNumber, RationalNumber)):
                epsilon = float(precision.value)
            elif isinstance(precision, (int, float)):
                epsilon = float(precision)
            else:
                raise TypeError("Precision must be an instance of FixedPrecision, FloatNumber, RationalNumber, int, or float")
        else:
            epsilon = 1e-15  # Default precision

        est_pi = 0.0
        k = 0
        while True:
            term = (factorial(6*k) * (13591409 + 545140134*k)) / (factorial(3*k) * factorial(k)**3 * (-640320)**(3*k))
            est_pi += term
            if abs(term) < epsilon:
                if output:
                    print("The upper bound is k=", k)
                break
            k += 1

        pi_value = 1.0 / ((np.sqrt(10005)/4270934400)  * est_pi)
        
        if typeoutput == "FixedPrecision":
            return FixedPrecision(float(pi_value), outputprec)
        elif typeoutput == "FloatNumber":
            return FloatNumber(float(pi_value))
        elif typeoutput == "Decimal":
            return Decimal( Decimal(pi_value).quantize(Decimal(1)/(10**Decimal(outputprec)) ))
        else:
            return float(pi_value)
    except Exception as e:
        print(f"An error occurred while computing Chudnovsky's pi: {e}")
        return None

