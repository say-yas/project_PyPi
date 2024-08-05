from src.FixedPrecision import FixedPrecision
from src.FloatNumber import FloatNumber
from src.RationalNumber import RationalNumber
from decimal import Decimal

def leibniz_pi(num_terms, typeoutput=float, outputprec=6):
    """
    Compute an approximation of pi using the Leibniz series.
    The formula is given by: pi = 4*sum_k (-1)^k/(2*k+1)
    input:  num_terms - number of terms in the series (can be int, float, FixedPrecision, FloatNumber, or RationalNumber)
            typeoutput (string) - the type of output ["FixedPrecision", "FloatNumber", "Decimal"]
            outputprec - the precision of output when type is decimal of fixed precision
    output: est_pi - approximation of pi (as a FixedPrecision instance with 6 decimal places)
    """
    try:
        if isinstance(num_terms, int):
            num_terms = int(num_terms)
        elif isinstance(num_terms, (float, FixedPrecision, FloatNumber)):
            num_terms = int(round(float(num_terms)))
        elif isinstance(num_terms, (RationalNumber)):
            num_terms = int(round(RationalNumber.tofloatnumber(num_terms)))
        else:
            raise TypeError("num_terms must be int, float, FixedPrecision, FloatNumber, or RationalNumber")

        est_pi = 0.0
        sign = 1.0
        for n in range(num_terms):
            est_pi += sign / (2.0 * n + 1.0)
            sign *= -1.0

        pi_lieb = 4.0 * est_pi
        if typeoutput=="FixedPrecision":
            return FixedPrecision(pi_lieb, outputprec)
        elif typeoutput=="FloatNumber":
            return FloatNumber(pi_lieb)
        elif typeoutput=="Decimal":
            return Decimal( Decimal(pi_lieb).quantize(Decimal(1)/(10**Decimal(outputprec)) ))
        else:
            return float(pi_lieb)
    except Exception as e:
        print("An error occurred:", e)
        return None
    
