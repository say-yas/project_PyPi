from PIapprox.continued_fraction_pi import continued_fraction_pi

try:
    for ndigit in range(12):
        pi_value = continued_fraction_pi(numdigit=ndigit, typeoutput="Fraction")
        if pi_value is not None:
            print(f"For ndigit={ndigit}, the approximation of pi reads: {pi_value}")

        pi_value = continued_fraction_pi(numdigit=ndigit, typeoutput="RationalNumber")
        if pi_value is not None:
            print(f"For ndigit={ndigit}, the approximation of pi reads:{pi_value}")

        pi_value = continued_fraction_pi(numdigit=ndigit, typeoutput="float")
        if pi_value is not None:
            print(f"For ndigit={ndigit}, the approximation of pi reads: {pi_value}")

        pi_value = continued_fraction_pi(numdigit=ndigit, typeoutput="FloatNumber")
        if pi_value is not None:
            print(f"For ndigit={ndigit}, the approximation of pi reads: {pi_value}")

        print("=====================================")
    

except Exception as e:
    print(f"An error occurred: {e}")