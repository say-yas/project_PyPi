import numpy as np
from src.FixedPrecision import FixedPrecision
from src.FloatNumber import FloatNumber
from src.RationalNumber import RationalNumber
from decimal import Decimal
from PIapprox.factorial import factorial

def ramanujan_pi(precision=None, typeoutput="Float", outputprec=6, output=False):
    """
    Compute an approximation of pi using Ramanujan's formula.

    The formula is given by:
    1/pi = ((2*sqrt(2)/9801 ) * sum_k (factorial(4*k)*(1103+26390*k))/(factorial(k)**4 * 396**(4*k)))

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
            term = (factorial(4*k) * (1103+26390*k)) / (factorial(k)**4 * 396**(4*k))
            est_pi += term
            if abs(term) < epsilon:
                if output:
                    print("The upper bound is k=", k)
                break
            k += 1

        pi_value = 1.0 / (2.0 * np.sqrt(2.0) / 9801 * est_pi)
        
        if typeoutput == "FixedPrecision":
            return FixedPrecision(float(pi_value), outputprec)
        elif typeoutput == "FloatNumber":
            return FloatNumber(float(pi_value))
        elif typeoutput == "Decimal":
            return Decimal( Decimal(pi_value).quantize(Decimal(1)/(10**Decimal(outputprec)) ))
        else:
            return float(pi_value)
    except Exception as e:
        print(f"An error occurred while computing Ramanujan's pi: {e}")
        return None
