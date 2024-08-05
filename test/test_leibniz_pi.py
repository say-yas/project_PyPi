from PIapprox.leibniz_pi import leibniz_pi
import numpy as np
from src.FixedPrecision import FixedPrecision

def test_leibniz_pi(num_terms0, typeoutput="float", outputprec=6):
    
    pi_approx = leibniz_pi(num_terms0, typeoutput=typeoutput, outputprec=outputprec)
    
    if typeoutput=="Decimal":
        print("Upperbound=",int(num_terms0),
          "terms: Leibniz approx. of pi=", pi_approx,
           ", |pi_approx-pi|=", np.abs(float(pi_approx) -np.pi))
    else:
        print("Upperbound=",int(num_terms0),
          "terms: Leibniz approx. of pi=", pi_approx,
           ", |pi_approx-pi|=", np.abs(pi_approx -np.pi))

    
try:
    for num_terms in [1e3, 1e4, 1e5, 1e6]:
        for typeoutput in ["FloatNumber", "float", "FixedPrecision", "Decimal"]:
            print(f"Testing with {num_terms} terms and typeoutput={typeoutput}")
            test_leibniz_pi(num_terms, typeoutput=typeoutput, outputprec=10)
        print("====================================")

except Exception as e:
    print(f"An error occurred: {e}")