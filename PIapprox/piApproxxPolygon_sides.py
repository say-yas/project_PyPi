import numpy as np
from decimal import Decimal, getcontext, InvalidOperation
from src.FixedPrecision import FixedPrecision
from src.FloatNumber import FloatNumber
from src.RationalNumber import RationalNumber

def approximate_pi_with_polygon(sides, typeoutput="float", outputprec=8):
    if sides < 3:
        raise ValueError("Number of sides must be greater than or equal to 3")
    try:
    
        if typeoutput == "Decimal":
            # getcontext().prec = outputprec
            side_length = Decimal(2.0) * Decimal( Decimal((np.sin(np.pi / sides))).quantize(Decimal(1)/(10**Decimal(outputprec)) ))
            dsides=  Decimal( sides)
            param = dsides * side_length
            approx_pi = param / Decimal(2.0)
            return Decimal( approx_pi.quantize(Decimal(1)/(10**Decimal(outputprec)) ))
        elif typeoutput == "FixedPrecision":
            
            side_length = 2.0 * FixedPrecision(np.sin(np.pi / sides), outputprec)
            param = FixedPrecision(sides, outputprec) * side_length
            approx_pi = param / 2.0
            approx_pi.decimal_places = outputprec
            return approx_pi
        elif typeoutput == "FloatNumber":
            side_length = 2 * FloatNumber(np.sin(np.pi / sides))
            param = FloatNumber(sides) * side_length
            approx_pi = param / 2.0
            return approx_pi
        else:
            side_length = 2.0 * np.sin(np.pi / sides)
            param = sides * side_length
            approx_pi = param / 2.0
            return float(approx_pi)
    except (OverflowError, InvalidOperation) as e:
        print(f"An error occurred while approximating π with a polygon of {sides} sides: {e}")
        return None

    