from PIapprox.piApproxMonte import MonteCarloApproximation
import numpy as np

def test_monte_carlo_approximation(num_points):
    monte_carlo_approximation = MonteCarloApproximation(num_points)
    approx_pi = monte_carlo_approximation.calculate_approximation(typeoutput="FixedPrecision", outputprec=6)
    if approx_pi is not None:
        approx_pi_float = float(approx_pi.value)
        print(f"Approximation of pi using Monte Carlo method with {num_points} points: {approx_pi}")
        print(f"Absolute error: {np.abs(approx_pi_float - np.pi)}")

num_points_values = [1e3, 1e4, 1e5, 1e6]
for num_points in num_points_values:
    test_monte_carlo_approximation(int(num_points))
    print()  # Add an empty line for better readability

try:
    num_points = 1000000
    approx_pi = MonteCarloApproximation(num_points).calculate_approximation(typeoutput="FloatNumber", outputprec=10)
    if approx_pi is not None:
        print(f"Approximation of pi FloatNumber precision 16: {approx_pi}")

    approx_pi = MonteCarloApproximation(num_points).calculate_approximation(typeoutput="float", outputprec=10)
    if approx_pi is not None:
        print(f"Approximation of pi Float precision 16: {approx_pi}")

    approx_pi = MonteCarloApproximation(num_points).calculate_approximation(typeoutput="Decimal", outputprec=16)
    if approx_pi is not None:
        print(f"Approximation of pi with 16 decimal places: {approx_pi}")

except Exception as e:
    print(f"An error occurred: {e}")