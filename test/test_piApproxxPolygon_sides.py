import unittest
import numpy as np
from decimal import Decimal, getcontext, InvalidOperation
from PIapprox.piApproxxPolygon_sides import approximate_pi_with_polygon
from src.FixedPrecision import FixedPrecision
from src.FloatNumber import FloatNumber

def test_approximate_pi_with_invalid_sides():
    try:
        num_sides_list = [3, 4, 5, 6, 7, 8]
        types = ['Decimal', 'FixedPrecision', 'FloatNumber']
        
        for sides in num_sides_list:
            print("Testing with sides:", sides)
            for typeoutput in types:
                pi_approx = approximate_pi_with_polygon(sides = sides, typeoutput=typeoutput)
                
                print(f"Approximation of π using a {sides}-sided polygon with type {typeoutput}: {pi_approx}")
            print("=====================================")
    except Exception as e:
        print(f"An error occurred during the various types test: {e}")
if __name__ == "__main__":
   

    print("\nTesting polygon approximation with invalid sides...")
    test_approximate_pi_with_invalid_sides()
