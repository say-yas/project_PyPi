import numpy as np
from src.FixedPrecision import FixedPrecision
from src.FloatNumber import FloatNumber
from decimal import Decimal

from PIapprox.chudnovsky_pi import chudnovsky_pi

def test_chudnovsky_pi(precision):
    pi_approx = chudnovsky_pi(precision=precision, typeoutput="float")
    print(f"Precision={precision}: Approximation of pi={pi_approx}, |pi_approx-pi|={np.abs(pi_approx - np.pi)}")

for precision in [1e-3, 1e-6, 1e-9, 1e-12]:
    test_chudnovsky_pi(precision)

try:
    pi_value = chudnovsky_pi(typeoutput="FloatNumber", outputprec=16)
    if pi_value is not None:
        print(f"Approximation of pi FloatNumber precision 16: {pi_value}")

    pi_value = chudnovsky_pi(typeoutput="float", outputprec=10)
    if pi_value is not None:
        print(f"Approximation of pi Float precision 10: {pi_value}")

    pi_value = chudnovsky_pi(typeoutput="Decimal", outputprec=16)
    if pi_value is not None:
        print(f"Approximation of pi with 16 decimal places: {pi_value}")

    pi_value = chudnovsky_pi(precision=1e-100, typeoutput="float", output=True)
    if pi_value is not None:
        print(f"Approximation of pi with high precision and output: {pi_value}")


except Exception as e:
    print(f"An error occurred: {e}")