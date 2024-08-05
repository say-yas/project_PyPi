from PIapprox.chudnovsky_pi import chudnovsky_pi

try:
    pi_value = chudnovsky_pi(typeoutput="FloatNumber", outputprec=10, output=True)
    if pi_value is not None:
        print(f"Approximation of pi: {pi_value}")
    pi_value = chudnovsky_pi(typeoutput="float", outputprec=10, output=True)
    if pi_value is not None:
        print(f"Approximation of pi: {pi_value}")

    outputprec = 16
    pi_value = chudnovsky_pi(typeoutput="FixedPrecision", outputprec=outputprec, output=True)
    if pi_value is not None:
        print(f"Approximation of pi with precision {outputprec}: {pi_value}")

    pi_value = chudnovsky_pi(typeoutput="Decimal", outputprec=outputprec, output=True)
    if pi_value is not None:
        print(f"Approximation of pi with precision {outputprec}: {pi_value}")
    

except Exception as e:
    print(f"An error occurred: {e}")