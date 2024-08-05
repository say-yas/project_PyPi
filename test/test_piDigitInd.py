from PIapprox.piDigitInd import PiCalculator
from src.FixedPrecision import FixedPrecision

try:
    precision = FixedPrecision(15, 0)  # 50 digits
    pi_calculator = PiCalculator(precision)
    pi_value = pi_calculator.compute_pi_digits(typeoutput="Float", outputprec=50)
    if pi_value is not None:
        print(f"Approximation of pi with precision {precision}: {pi_value}")

except Exception as e:
    print(f"An error occurred: {e}")