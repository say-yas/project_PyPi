# ProjectPi24_Hammad_Sayyad

This is a package that computes the pi number using various approaches.
The codes are implimented by <ins>Muhammad Hammad</ins> and <ins>Sharareh Sayyad</ins>.

## Summary: 
To run all tests, use `sh script_test_piapprox.sh` or make the bash script executable using `chmod+x script_test_piapprox.sh`
To run all implimentations, use `sh create_modules.sh`

Demonstration of the methods and analyzing their performance is presented in a [Jupyter notebook](examples/Demostration_pi_approximations.ipynb) in the `example` directory.

## Collection of algorithms for estimating the pi number

Our methods for evaluating $\pi$ benefit from using `polygons`, `Monte Carlo algorithm`, `continued-fraction approach`, `Ramanujan's formula`, `Leibniz formula`, `Chudnovsky formula`, `Bailey–Borwein–Plouffe formula (BBP) fromula`, `Gauss-Legendre algorithm` and `Nilakantha series`. One can find the implimentation in [PIapprox](PIapprox/) directory.

## Project contains:


- Class for types of outputs 

    * [Rationals](src/RationalNumber.py)

    * [Floats](src/FloatNumber.py)

    * [Fix precision numbers](src/RationalNumber.py)

    * [A comparison with standard Python implementation of the previous three classes](examples/Demostration_pi_approximations.ipynb)

- Class for approximations of pi

    * [Approximation of pi using polygons](PIapprox/piApproxxPolygon.py) and [polygon (sides)](PIapprox/piApproxxPolygon_sides)

    * [Approximation of pi using Monte-Carl methods](PIapprox/piApproxMonte.py)

    * [Computing the digits of pi independently](PIapprox/piDigitFormulas.py)

    * [Ramanujan series](PIapprox/ramanujan_pi.py)

    * [Chudnovsky](PIapprox/chudnovsky_pi.py)

    * [BBP approach](PIapprox/BBP_pi.py)

    * [Continued fraction](PIapprox/continued_fraction_pi.py)

    * [Leibniz formula](PIapprox/leibniz_pi.py)


## Summary:
In summary the project consists of the following components: 

• Classes that approximate numbers,

• Methods that rely on these classes to approximate pi,

• An automated test suite for[FloatNumber](test/test_unittest_floatnumber.py), [RationalNumber](test/test_unittest_rationalnumber.py) and [FixedPrecision](test/test_unittest_fixedpercision.py),

• A Jupyter notebook that explains the methods and the comparison.

