from PIapprox.piDigitFormulas import PiCalculator
import numpy as np


try:

    num_digits = int(30)
    pi_calculator = PiCalculator(num_digits)

    pi_gauss_legendre = pi_calculator.compute_pi_gauss_legendre(typeoutput="FloatNumber", outputprec=num_digits)
    if pi_gauss_legendre is not None:
        print(f"Approximation of pi (Gauss-Legendre algorithm): {pi_gauss_legendre}")

    pi_gauss_legendre = pi_calculator.compute_pi_gauss_legendre(typeoutput="float", outputprec=num_digits)
    if pi_gauss_legendre is not None:
        print(f"Approximation of pi (Gauss-Legendre algorithm): {pi_gauss_legendre}")

    pi_gauss_legendre = pi_calculator.compute_pi_gauss_legendre(typeoutput="Decimal", outputprec=num_digits)
    if pi_gauss_legendre is not None:
        print(f"Approximation of pi (Gauss-Legendre algorithm) with {num_digits} digits: {pi_gauss_legendre}")

    pi_gauss_legendre = pi_calculator.compute_pi_gauss_legendre(typeoutput="FixedPrecision", outputprec=num_digits)
    if pi_gauss_legendre is not None:
        print(f"Approximation of pi (Gauss-Legendre algorithm) with {num_digits} digits: {pi_gauss_legendre}")


    pi_nilakantha = pi_calculator.compute_pi_nilakantha(typeoutput="float", outputprec=num_digits )
    if pi_nilakantha is not None:
        print(f"Approximation of pi (Nilakantha series): {pi_nilakantha}")

    pi_nilakantha = pi_calculator.compute_pi_nilakantha(typeoutput="FloatNumber", outputprec=num_digits )
    if pi_nilakantha is not None:
        print(f"Approximation of pi (Nilakantha series): {pi_nilakantha}")

    pi_nilakantha = pi_calculator.compute_pi_nilakantha(typeoutput="Decimal", outputprec=num_digits )
    if pi_nilakantha is not None:
        print(f"Approximation of pi (Nilakantha series) with {num_digits} digits: {pi_nilakantha}")

    pi_nilakantha = pi_calculator.compute_pi_nilakantha(typeoutput="FixedPrecision", outputprec=num_digits )
    if pi_nilakantha is not None:
        print(f"Approximation of pi (Nilakantha series) with {num_digits} digits: {pi_nilakantha}")


except Exception as e:
    print(f"An error occurred in the main execution: {e}")

