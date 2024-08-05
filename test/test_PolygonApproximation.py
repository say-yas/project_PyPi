import numpy as np
from decimal import Decimal, getcontext, InvalidOperation
from PIapprox.piApproxxPolygon import PolygonApproximation
from src.FixedPrecision import FixedPrecision

def test_polygon_approximation_with_precision():
    try:
        sides = FixedPrecision(4, 0)
        precision = FixedPrecision(1e-6, 6)
        approximator = PolygonApproximation(sides)
        approximator.calculate_approximations(precision)
        
        print("Approximations of π with increasing polygon sides:")
        for sides, approx in approximator.approximations:
            print(f"Sides: {sides}, Approximation: {approx}, Error: {abs(approx - np.pi)}")
        
        approximator.plot_approximations('pi_approximations_precision.png')
        print("Polygon approximation test with precision completed successfully.")
    except Exception as e:
        print(f"An error occurred during the precision test: {e}")

def test_polygon_approximation_with_fixed_sides():
    try:
        fixed_values = {'sides': [3, 4, 5, 6, 7, 8, 16, 32, 64, 128, 256, 512, 1024]}
        sides = FixedPrecision(4, 0)
        precision = FixedPrecision(1e-6, 6)
        
        approximator = PolygonApproximation(sides)
        approximator.calculate_approximations(precision, fixed_values=fixed_values)
        
        print("Fixed sides approximations of π:")
        for sides, approx in approximator.approximations:
            print(f"Sides: {sides}, Approximation: {approx}, Error: {abs(approx - np.pi)}")
        
        approximator.plot_runtimes('pi_runtimes_fixed_sides.png')
        print("Polygon approximation test with fixed sides completed successfully.")
    except Exception as e:
        print(f"An error occurred during the fixed sides test: {e}")

def test_polygon_approximation_with_various_types():
    try:
        num_sides_list = [3, 4, 5, 6, 7, 8]
        types = ['Decimal', 'FixedPrecision', 'FloatNumber']
        print("Testing with sides:", num_sides_list)
        
        for sides in num_sides_list:
            approximator = PolygonApproximation(sides)
            for typeoutput in types:
                pi_approx = approximator.approximate_pi_with_polygon(typeoutput=typeoutput)
                
                print(f"Approximation of π using a {sides}-sided polygon with type {typeoutput}: {pi_approx}")
    except Exception as e:
        print(f"An error occurred during the various types test: {e}")

if __name__ == "__main__":
    print("Testing polygon approximation with precision...")
    test_polygon_approximation_with_precision()

    print("\nTesting polygon approximation with fixed sides...")
    test_polygon_approximation_with_fixed_sides()

    print("\nTesting polygon approximation with various types...")
    test_polygon_approximation_with_various_types()