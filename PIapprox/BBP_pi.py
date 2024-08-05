import numpy as np
from src.FixedPrecision import FixedPrecision
from src.FloatNumber import FloatNumber
from src.RationalNumber import RationalNumber
from decimal import Decimal

def bbp_pi(precision=None, typeoutput="FixedPrecision", outputprec=6, output=False):
    """
    Compute an approximation of pi using BBP digit extraction algorithm.

    The formula is given by:
    pi = sum_k 16^-k * (4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6))

    Args:
    precision: The desired precision, an instance of FixedPrecision, FloatNumber, RationalNumber, int, or float.
    typeoutput: The type of output ("FixedPrecision", "FloatNumber", "Decimal", or "float").
    outputprec: The precision of the output when type is "FixedPrecision" or "Decimal".
    output: Whether to output the upper bound for the approximation.

    Returns:
    est_pi: Approximation of pi with the specified precision and output type.
    """
    
    try:
        if(typeoutput == "Decimal" and outputprec>15):
            raise ValueError("The maximum precision for Decimal is less than 15")
        
        if precision is not None:
            if typeoutput == "FixedPrecision":
                epsilon = FixedPrecision(precision, outputprec) 
            elif typeoutput == "FloatNumber":
                epsilon = FloatNumber(precision) 
            elif typeoutput == "Decimal":
                
                epsilon = Decimal( Decimal(precision).quantize(Decimal(1)/(10**Decimal(outputprec)) ))
            else:
                epsilon = float(precision)
        else:
            epsilon = 1e-15  # Default precision

        if typeoutput == "FixedPrecision":
            est_pi = FixedPrecision(0.0, outputprec) 
        elif typeoutput == "FloatNumber":
            est_pi = FloatNumber(0.0) 
        elif typeoutput == "Decimal":
            est_pi = Decimal( Decimal(0.0).quantize(Decimal(1)/(10**Decimal(outputprec)) ))
        else:
            est_pi = float(0.0)
        

        k = 0
        while True:

            if typeoutput == "FixedPrecision":
                term = FixedPrecision((4/(8*k+1) ), outputprec) / FixedPrecision((16**k), outputprec) 
                term += FixedPrecision((- 2/(8*k+4) ), outputprec) / FixedPrecision((16**k), outputprec) 
                term += FixedPrecision((- 1/(8*k+5) ), outputprec) / FixedPrecision((16**k), outputprec) 
                term += FixedPrecision((- 1/(8*k+6)), outputprec) / FixedPrecision((16**k), outputprec) 
            elif typeoutput == "FloatNumber":
                term = FloatNumber((4/(8*k+1) )) / FloatNumber((16**k)) 
                term += FloatNumber((- 2/(8*k+4))) / FloatNumber((16**k)) 
                term += FloatNumber((- 1/(8*k+5) )) / FloatNumber((16**k)) 
                term += FloatNumber((- 1/(8*k+6))) / FloatNumber((16**k)) 
            elif typeoutput == "Decimal":
                deno =  Decimal( Decimal((16**k)).quantize(Decimal(1)/(10**Decimal(outputprec)) ))
                term =  Decimal( Decimal( Decimal((4/(8*k+1))) / deno).quantize(Decimal(1)/(10**Decimal(outputprec)) ))
                term += Decimal( Decimal( Decimal((- 2/(8*k+4))) / deno).quantize(Decimal(1)/(10**Decimal(outputprec)) ) )
                term += Decimal( Decimal( Decimal((- 1/(8*k+5))) / deno).quantize(Decimal(1)/(10**Decimal(outputprec)) ) )
                term += Decimal( Decimal( Decimal((- 1/(8*k+6))) / deno).quantize(Decimal(1)/(10**Decimal(outputprec)) ) )
            else:
                term = float((4.0/(8.0*k+1.0) - 2.0/(8.0*k+4.0) - 1.0/(8.0*k+5.0) - 1.0/(8.0*k+6.0))/(16**k))
        
            est_pi += term
            if abs(term) < epsilon:
                if output:
                    print("The upper bound is k=", k)
                break
            k += 1

        pi_value =  est_pi

        if typeoutput == "FixedPrecision":
            return FixedPrecision(pi_value.value, outputprec) 
        elif typeoutput == "FloatNumber":
            return pi_value
        elif typeoutput == "Decimal":
            return Decimal( pi_value.quantize(Decimal(1)/(10**Decimal(outputprec)) )) 
        else:
            return float(pi_value)
    except Exception as e:
        print(f"An error occurred while computing BBP's pi: {e}")
        return None


