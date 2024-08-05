from PIapprox.ramanujan_pi import ramanujan_pi
import numpy as np
from src.FixedPrecision import FixedPrecision

def test_ramanujan_pi():
    
    pi_approx = ramanujan_pi()
    print("terms: ramanujan approx. of pi=", pi_approx,
           ", |pi_approx-pi|=", np.abs(pi_approx -np.pi))

try:
    test_ramanujan_pi()

    precision = 10
    pi_value = ramanujan_pi(typeoutput="FloatNumber", outputprec=precision, output=True)
    if pi_value is not None:
        print(f"Approximation of pi with FloatNumber precision {precision}: {pi_value}")

    pi_value = ramanujan_pi(typeoutput="float", outputprec=precision, output=True)
    if pi_value is not None:
        print(f"Approximation of pi with Float precision {precision}: {pi_value}")

    #
    pi_value = ramanujan_pi(precision, typeoutput="FixedPrecision", outputprec=precision, output=True)
    if pi_value is not None:
        print(f"Approximation of pi with FixedPrecision precision {precision}: {pi_value}")

    pi_value = ramanujan_pi(precision, typeoutput="Decimal", outputprec=precision, output=True)
    if pi_value is not None:
        print(f"Approximation of pi with Decimal precision {precision}: {pi_value}")

except Exception as e:
    print(f"An error occurred: {e}")