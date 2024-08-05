import numpy as np

from fractions import Fraction
from decimal import Decimal

from src.FixedPrecision import FixedPrecision
from src.FloatNumber import FloatNumber
from src.RationalNumber import RationalNumber



from PIapprox.piApproxxPolygon import PolygonApproximation
from PIapprox.continued_fraction_pi import continued_fraction_pi
from PIapprox.leibniz_pi import leibniz_pi
from PIapprox.piApproxMonte import MonteCarloApproximation
from PIapprox.piDigitFormulas import PiCalculator
from PIapprox.piApproxxPolygon_sides import approximate_pi_with_polygon

import matplotlib.pyplot as plt

import time



def data_collection_poly_sides(typeoutput, outputprec):
    """
    Thi function collects the data for the polygon approximation of pi
    params: typeoutput: str: the type of output to be used
            outputprec: int: the precision of the output
    """

    pi_est=[]
    for num_sides in range(3, 200, 10):
        
        start_time = time.time()
        pi_approx = approximate_pi_with_polygon(sides=num_sides, typeoutput=typeoutput, outputprec=outputprec)
        time_est_pi = time.time() - start_time

        if typeoutput=="Decimal":
            err = np.abs(pi_approx - Decimal(np.pi))
        else:
            err = np.abs(pi_approx -np.pi)

        pi_est.append([int(num_sides), pi_approx, err, time_est_pi])

    return pi_est



def plot_poly_sides(outputprec):
    """
    This function plots the Nilakantha series.
    params: outputprec: int: the precision of the output
    """
        
    pivals_floatnum = data_collection_poly_sides("FloatNumber", outputprec)
    pivals_float = data_collection_poly_sides("float", outputprec)

    pivals_decimal = data_collection_poly_sides("Decimal", outputprec)
    pivals_fixedpr = data_collection_poly_sides("FixedPrecision", outputprec)

    numterm = [n for n, _,_,_ in pivals_floatnum]

    p_fixedpr = [approx for _, approx,_,_ in pivals_fixedpr]
    p_decimal= [approx for _, approx,_,_ in pivals_decimal]
    p_float = [approx for _, approx,_,_ in pivals_float]
    p_floatnum = [approx for _, approx,_,_ in pivals_floatnum]

    err_fixedpr = [approx for _,_,approx,_ in pivals_fixedpr]
    err_decimal= [approx for _,_,approx,_ in pivals_decimal]
    err_float = [approx for _,_,approx,_ in pivals_float]
    err_floatnum = [approx for _,_,approx,_ in pivals_floatnum]

    t_fixedpr = [approx for _,_,_,approx in pivals_fixedpr]
    t_decimal= [approx for _,_,_,approx in pivals_decimal]
    t_float = [approx for _,_,_,approx in pivals_float]
    t_floatnum = [approx for _,_,_,approx in pivals_floatnum]

    fig, axs = plt.subplots(nrows=1,ncols=3, figsize=(12, 4))

    axs[0].plot(numterm, p_float, marker='o')
    axs[0].axhline(y=np.pi, color='r', linestyle='--', label=r'$\pi_{numpy}$')
    axs[0].set_xlabel('Number of sides')
    axs[0].set_ylabel(r'Approximation of $\pi$')
    axs[0].set_title(r'Approximating $\pi$ using polygons')
    axs[0].legend()
    axs[0].set_xscale('log', base=10)

    axs[1].plot(numterm, err_float, marker='o', label='float')
    axs[1].plot(numterm, err_floatnum, marker='o', label='FloatNumber')
    axs[1].plot(numterm, err_fixedpr, marker='o', label='FixedPrecision')
    axs[1].plot(numterm, err_decimal, marker='o', label='Decimal')
    axs[1].set_xlabel('Number of sides')
    axs[1].set_ylabel(r'$|\pi_{approx} -\pi_{numpy}|$')
    axs[1].set_title(f'Error of the Approximation with precision {outputprec}')
    axs[1].legend()
    axs[1].set_xscale('log', base=10)
    axs[1].set_yscale('log', base=10)


    axs[2].plot(numterm, t_float, marker='o', label='float')
    axs[2].plot(numterm, t_floatnum, marker='o', label='FloatNumber')
    axs[2].plot(numterm, t_fixedpr, marker='o', label='FixedPrecision')
    axs[2].plot(numterm, t_decimal, marker='o', label='Decimal')
    axs[2].set_xlabel('Number of sides')
    axs[2].set_ylabel(r'$\Delta t$')
    axs[2].set_title(r'Runtime of the Approximation')
    axs[2].legend()
    axs[2].set_xscale('log', base=10)
    axs[2].set_yscale('log', base=10)

    fig.tight_layout()
    plt.show()


def plot_approxs_polygon(approximator):
        """
        Plot the approximations of pi using the polygon method.
        params: approximator: PolygonApproximation: the approximator object
        """
        try:

            sides = [n for n, _ in approximator.approximations]
            approximations = [approx for _, approx in approximator.approximations]

            fig, axs = plt.subplots(nrows=1,ncols=2, figsize=(8, 4))

            axs[0].plot(sides, approximations, marker='o')
            axs[0].axhline(y=np.pi, color='r', linestyle='--', label=r'$\pi_{numpy}$')
            axs[0].set_xlabel('Number of sides')
            axs[0].set_ylabel(r'Approximation of $\pi$')
            axs[0].set_title(r'Approximating $\pi$ using Polygons')
            axs[0].legend()
            # axs[0].grid(True)
            axs[0].set_xscale('log', base=2)

            axs[1].plot(sides, [abs(approx - np.pi) for approx in approximations], marker='o')
            axs[1].set_xlabel('Number of sides')
            axs[1].set_ylabel(r'$|\pi_{approx} -\pi_{numpy}|$')
            axs[1].set_title('Error of the Approximation')
            axs[1].grid(True)
            axs[1].set_xscale('log', base=2)
            axs[1].set_yscale('log', base=10)

            fig.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting the approximations: {e}")

def plot_approxs_confrac(maxnumdigit=10):
        """
        Plot the approximations of pi using the polygon method.
        params: maxnumdigit: int: the maximum number of digits to be used
        """
        try:

            pivals_frac = []
            pivals_ratnum = []
            for ndigit in range(maxnumdigit):
                pivals_frac.append( [ndigit, continued_fraction_pi(numdigit=ndigit, typeoutput="Fraction") ])
                pivals_ratnum.append( [ndigit, continued_fraction_pi(numdigit=ndigit, typeoutput="RationalNumber")] )

            digts = [n for n, _ in pivals_frac]
            approxs_frac = [approx for _, approx in pivals_frac]
            approxs_ratnum = [approx for _, approx in pivals_ratnum]

            fig, axs = plt.subplots(nrows=1,ncols=2, figsize=(8, 4))

            axs[0].plot(digts, approxs_frac, marker='o')
            axs[0].axhline(y=np.pi, color='r', linestyle='--', label=r'$\pi_{numpy}$')
            axs[0].set_xlabel('Number of digits')
            axs[0].set_ylabel(r'Approximation of $\pi$')
            axs[0].set_title(r'Approximating $\pi$ using Continued fractions')
            axs[0].legend()

            axs[1].plot(digts, [abs(approx - np.pi) for approx in approxs_frac], marker='o')
            axs[1].set_xlabel('Number of digits')
            axs[1].set_ylabel(r'$|\pi_{approx} -\pi_{numpy}|$')
            axs[1].set_title('Error of the Approximation')
            axs[1].grid(True)
            axs[1].set_yscale('log', base=10)

            fig.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting the approximations: {e}")

def plot_time_approxs_confrac(maxnumdigit=10):
    """
    Plot the approximations of pi using the polygon method.
    params: maxnumdigit: int: the maximum number of digits to be used
    """
    try:

        time_pivals_frac = []
        time_pivals_ratnum = []
        time_pivals_float = []
        time_pivals_floatnum = []
        for ndigit in range(maxnumdigit):
            start_time = time.time()
            valpi = continued_fraction_pi(numdigit=ndigit, typeoutput="Fraction") 
            time_est_pi = time.time() - start_time
            time_pivals_frac.append( [ndigit, time_est_pi])

            start_time = time.time()
            valpi = continued_fraction_pi(numdigit=ndigit, typeoutput="RationalNumber")
            time_est_pi = time.time() - start_time
            time_pivals_ratnum.append( [ndigit, time_est_pi] )

            start_time = time.time()
            valpi = continued_fraction_pi(numdigit=ndigit, typeoutput="float")
            time_est_pi = time.time() - start_time
            time_pivals_float.append( [ndigit, time_est_pi] )

            start_time = time.time()
            valpi = continued_fraction_pi(numdigit=ndigit, typeoutput="FloatNumber")
            time_est_pi = time.time() - start_time
            time_pivals_floatnum.append( [ndigit, time_est_pi] )

        digts = [n for n, _ in time_pivals_frac]
        t_frac = [approx for _, approx in time_pivals_frac]
        t_ratnum = [approx for _, approx in time_pivals_ratnum]
        t_float = [approx for _, approx in time_pivals_float]
        t_floatnum = [approx for _, approx in time_pivals_floatnum]

        fig, axs = plt.subplots(nrows=1,ncols=1, figsize=(4, 4))

        axs.plot(digts, t_frac, marker='o', label="Fraction(python)")
        axs.plot(digts, t_float, marker='x', label="float(python)")
        axs.plot(digts, t_ratnum, marker='s', label="RationalNumber(ours)")
        axs.plot(digts, t_floatnum, marker='*', label="FloatNumber(ours)")
        
        axs.set_xlabel('Number of digits')
        axs.set_ylabel(r'$\Delta t$[sec]')
        axs.set_title(r'Run-time for estimating $\pi$ using continued fractions')
        axs.legend(bbox_to_anchor=(1.01, 0.7))
        axs.set_yscale('log', base=10)
        axs.grid(True)

        
        plt.show()
    except Exception as e:
        print(f"An error occurred while plotting the approximations: {e}")

def data_collection_leibniz(typeoutput, outputprec):
    """
    This function collects the data for the Leibniz approximation.
    params: typeoutput: str: the type of output to be used
            outputprec: int: the precision of the output
    """

    pi_est=[]
    for num_terms in [1, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]:
        
        start_time = time.time()
        pi_approx = leibniz_pi(num_terms, typeoutput=typeoutput, outputprec=outputprec)
        time_est_pi = time.time() - start_time

        if typeoutput=="Decimal":
            err = np.abs(pi_approx - Decimal(np.pi))
        else:
            err = np.abs(pi_approx -np.pi)

        pi_est.append([int(num_terms), pi_approx, err, time_est_pi])

    return pi_est

def plot_leibniz(outputprec):
    """
    This function plots the Leibniz approximation.
    params: outputprec: int: the precision of the output
    """
        
    pivals_floatnum = data_collection_leibniz("FloatNumber", outputprec)
    pivals_float = data_collection_leibniz("float", outputprec)

    pivals_decimal = data_collection_leibniz("Decimal", outputprec)
    pivals_fixedpr = data_collection_leibniz("FixedPrecision", outputprec)

    numterm = [n for n, _,_,_ in pivals_floatnum]

    p_fixedpr = [approx for _, approx,_,_ in pivals_fixedpr]
    p_decimal= [approx for _, approx,_,_ in pivals_decimal]
    p_float = [approx for _, approx,_,_ in pivals_float]
    p_floatnum = [approx for _, approx,_,_ in pivals_floatnum]

    err_fixedpr = [approx for _,_,approx,_ in pivals_fixedpr]
    err_decimal= [approx for _,_,approx,_ in pivals_decimal]
    err_float = [approx for _,_,approx,_ in pivals_float]
    err_floatnum = [approx for _,_,approx,_ in pivals_floatnum]

    t_fixedpr = [approx for _,_,_,approx in pivals_fixedpr]
    t_decimal= [approx for _,_,_,approx in pivals_decimal]
    t_float = [approx for _,_,_,approx in pivals_float]
    t_floatnum = [approx for _,_,_,approx in pivals_floatnum]

    fig, axs = plt.subplots(nrows=1,ncols=3, figsize=(12, 4))

    axs[0].plot(numterm, p_float, marker='o')
    axs[0].axhline(y=np.pi, color='r', linestyle='--', label=r'$\pi_{numpy}$')
    axs[0].set_xlabel('Number of terms')
    axs[0].set_ylabel(r'Approximation of $\pi$')
    axs[0].set_title(r'Approximating $\pi$ using Leinbiz formula')
    axs[0].legend()
    axs[0].set_xscale('log', base=10)

    axs[1].plot(numterm, err_float, marker='o', label='float')
    axs[1].plot(numterm, err_floatnum, marker='o', label='FloatNumber')
    axs[1].plot(numterm, err_fixedpr, marker='o', label='FixedPrecision')
    axs[1].plot(numterm, err_decimal, marker='o', label='Decimal')
    axs[1].set_xlabel('Number of terms')
    axs[1].set_ylabel(r'$|\pi_{approx} -\pi_{numpy}|$')
    axs[1].set_title(r'Error of the Approximation')
    axs[1].legend()
    axs[1].set_xscale('log', base=10)
    axs[1].set_yscale('log', base=10)


    axs[2].plot(numterm, t_float, marker='o', label='float')
    axs[2].plot(numterm, t_floatnum, marker='o', label='FloatNumber')
    axs[2].plot(numterm, t_fixedpr, marker='o', label='FixedPrecision')
    axs[2].plot(numterm, t_decimal, marker='o', label='Decimal')
    axs[2].set_xlabel('Number of terms')
    axs[2].set_ylabel(r'$\Delta t$')
    axs[2].set_title(r'Runtime of the Approximation')
    axs[2].legend()
    axs[2].set_xscale('log', base=10)
    axs[2].set_yscale('log', base=10)

    fig.tight_layout()
    plt.show()

def data_collection_mc(typeoutput, outputprec):

    pi_est=[]
    for num_points in [1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8]:
        
        start_time = time.time()
        mc_approx = MonteCarloApproximation(int(num_points))
        pi_approx = mc_approx.calculate_approximation(typeoutput=typeoutput, outputprec=outputprec)
        time_est_pi = time.time() - start_time

        if typeoutput=="Decimal":
            err = np.abs(pi_approx - Decimal(np.pi))
        else:
            err = np.abs(pi_approx -np.pi)

        pi_est.append([int(num_points), pi_approx, err, time_est_pi])

    return pi_est

def plot_mc(outputprec):
    """
    This function plots the Monte Carlo approximation.
    params: outputprec: int: the precision of the output
    """
        
    pivals_floatnum = data_collection_mc("FloatNumber", outputprec)
    pivals_float = data_collection_mc("float", outputprec)

    pivals_decimal = data_collection_mc("Decimal", outputprec)
    pivals_fixedpr = data_collection_mc("FixedPrecision", outputprec)

    numterm = [n for n, _,_,_ in pivals_floatnum]

    p_fixedpr = [approx for _, approx,_,_ in pivals_fixedpr]
    p_decimal= [approx for _, approx,_,_ in pivals_decimal]
    p_float = [approx for _, approx,_,_ in pivals_float]
    p_floatnum = [approx for _, approx,_,_ in pivals_floatnum]

    err_fixedpr = [approx for _,_,approx,_ in pivals_fixedpr]
    err_decimal= [approx for _,_,approx,_ in pivals_decimal]
    err_float = [approx for _,_,approx,_ in pivals_float]
    err_floatnum = [approx for _,_,approx,_ in pivals_floatnum]

    t_fixedpr = [approx for _,_,_,approx in pivals_fixedpr]
    t_decimal= [approx for _,_,_,approx in pivals_decimal]
    t_float = [approx for _,_,_,approx in pivals_float]
    t_floatnum = [approx for _,_,_,approx in pivals_floatnum]

    fig, axs = plt.subplots(nrows=1,ncols=3, figsize=(12, 4))

    axs[0].plot(numterm, p_float, marker='o')
    axs[0].axhline(y=np.pi, color='r', linestyle='--', label=r'$\pi_{numpy}$')
    axs[0].set_xlabel('Number of points')
    axs[0].set_ylabel(r'Approximation of $\pi$')
    axs[0].set_title(r'Approximating $\pi$ using Monte Carlo approach')
    axs[0].legend()
    axs[0].set_xscale('log', base=10)

    axs[1].plot(numterm, err_float, marker='o', label='float')
    axs[1].plot(numterm, err_floatnum, marker='o', label='FloatNumber')
    axs[1].plot(numterm, err_fixedpr, marker='o', label='FixedPrecision')
    axs[1].plot(numterm, err_decimal, marker='o', label='Decimal')
    axs[1].set_xlabel('Number of points')
    axs[1].set_ylabel(r'$|\pi_{approx} -\pi_{numpy}|$')
    axs[1].set_title(r'Error of the Approximation')
    axs[1].legend()
    axs[1].set_xscale('log', base=10)
    axs[1].set_yscale('log', base=10)


    axs[2].plot(numterm, t_float, marker='o', label='float')
    axs[2].plot(numterm, t_floatnum, marker='o', label='FloatNumber')
    axs[2].plot(numterm, t_fixedpr, marker='o', label='FixedPrecision')
    axs[2].plot(numterm, t_decimal, marker='o', label='Decimal')
    axs[2].set_xlabel('Number of points')
    axs[2].set_ylabel(r'$\Delta t$')
    axs[2].set_title(r'Runtime of the Approximation')
    axs[2].legend()
    axs[2].set_xscale('log', base=10)
    axs[2].set_yscale('log', base=10)

    fig.tight_layout()
    plt.show()

def data_collection_nik(typeoutput, outputprec):
    """
    Thi function collects the data for the Nilakantha series.
    params: typeoutput: str: the type of output to be used
            outputprec: int: the precision of the output
    """

    pi_est=[]
    for num_digits in range(1, 120, 10):
        
        start_time = time.time()
        pi_calculator = PiCalculator(int(num_digits))
        pi_approx = pi_calculator.compute_pi_nilakantha(typeoutput=typeoutput, outputprec=outputprec)
        time_est_pi = time.time() - start_time

        if typeoutput=="Decimal":
            err = np.abs(pi_approx - Decimal(np.pi))
        else:
            err = np.abs(pi_approx -np.pi)

        pi_est.append([int(num_digits), pi_approx, err, time_est_pi])

    return pi_est

def plot_nik(outputprec):
    """
    This function plots the Nilakantha series.
    params: outputprec: int: the precision of the output
    """
        
    pivals_floatnum = data_collection_gl("FloatNumber", outputprec)
    pivals_float = data_collection_gl("float", outputprec)

    pivals_decimal = data_collection_gl("Decimal", outputprec)
    pivals_fixedpr = data_collection_gl("FixedPrecision", outputprec)

    numterm = [n for n, _,_,_ in pivals_floatnum]

    p_fixedpr = [approx for _, approx,_,_ in pivals_fixedpr]
    p_decimal= [approx for _, approx,_,_ in pivals_decimal]
    p_float = [approx for _, approx,_,_ in pivals_float]
    p_floatnum = [approx for _, approx,_,_ in pivals_floatnum]

    err_fixedpr = [approx for _,_,approx,_ in pivals_fixedpr]
    err_decimal= [approx for _,_,approx,_ in pivals_decimal]
    err_float = [approx for _,_,approx,_ in pivals_float]
    err_floatnum = [approx for _,_,approx,_ in pivals_floatnum]

    t_fixedpr = [approx for _,_,_,approx in pivals_fixedpr]
    t_decimal= [approx for _,_,_,approx in pivals_decimal]
    t_float = [approx for _,_,_,approx in pivals_float]
    t_floatnum = [approx for _,_,_,approx in pivals_floatnum]

    fig, axs = plt.subplots(nrows=1,ncols=3, figsize=(12, 4))

    axs[0].plot(numterm, p_float, marker='o')
    axs[0].axhline(y=np.pi, color='r', linestyle='--', label=r'$\pi_{numpy}$')
    axs[0].set_xlabel('Number of digits')
    axs[0].set_ylabel(r'Approximation of $\pi$')
    axs[0].set_title(r'Approximating $\pi$ using Nilakantha series')
    axs[0].legend()
    axs[0].set_xscale('log', base=10)

    axs[1].plot(numterm, err_float, marker='o', label='float')
    axs[1].plot(numterm, err_floatnum, marker='o', label='FloatNumber')
    axs[1].plot(numterm, err_fixedpr, marker='o', label='FixedPrecision')
    axs[1].plot(numterm, err_decimal, marker='o', label='Decimal')
    axs[1].set_xlabel('Number of digits')
    axs[1].set_ylabel(r'$|\pi_{approx} -\pi_{numpy}|$')
    axs[1].set_title(f'Error of the Approximation with precision {outputprec}')
    axs[1].legend()
    axs[1].set_xscale('log', base=10)
    axs[1].set_yscale('log', base=10)


    axs[2].plot(numterm, t_float, marker='o', label='float')
    axs[2].plot(numterm, t_floatnum, marker='o', label='FloatNumber')
    axs[2].plot(numterm, t_fixedpr, marker='o', label='FixedPrecision')
    axs[2].plot(numterm, t_decimal, marker='o', label='Decimal')
    axs[2].set_xlabel('Number of digits')
    axs[2].set_ylabel(r'$\Delta t$')
    axs[2].set_title(r'Runtime of the Approximation')
    axs[2].legend()
    axs[2].set_xscale('log', base=10)
    axs[2].set_yscale('log', base=10)

    fig.tight_layout()
    plt.show()

def data_collection_gl(typeoutput, outputprec):
    """
    The function collects the data for the Gauss-Legendre algorithm.
    params: typeoutput: str: the type of output to be used
            outputprec: int: the precision of the output
    """

    pi_est=[]
    for num_digits in range(1, 120, 5):
        
        start_time = time.time()
        pi_calculator = PiCalculator(int(num_digits))
        pi_approx = pi_calculator.compute_pi_gauss_legendre(typeoutput=typeoutput, outputprec=outputprec)
        time_est_pi = time.time() - start_time

        if typeoutput=="Decimal":
            err = np.abs(pi_approx - Decimal(np.pi))
        else:
            err = np.abs(pi_approx -np.pi)

        pi_est.append([int(num_digits), pi_approx, err, time_est_pi])

    return pi_est

def plot_gl(outputprec):
    """
    This function plots the Gauss-Legendre algorithm.
    params: outputprec: int: the precision of the output
    """
        
    pivals_floatnum = data_collection_gl("FloatNumber", outputprec)
    pivals_float = data_collection_gl("float", outputprec)

    pivals_decimal = data_collection_gl("Decimal", outputprec)
    pivals_fixedpr = data_collection_gl("FixedPrecision", outputprec)

    numterm = [n for n, _,_,_ in pivals_floatnum]

    p_fixedpr = [approx for _, approx,_,_ in pivals_fixedpr]
    p_decimal= [approx for _, approx,_,_ in pivals_decimal]
    p_float = [approx for _, approx,_,_ in pivals_float]
    p_floatnum = [approx for _, approx,_,_ in pivals_floatnum]

    err_fixedpr = [approx for _,_,approx,_ in pivals_fixedpr]
    err_decimal= [approx for _,_,approx,_ in pivals_decimal]
    err_float = [approx for _,_,approx,_ in pivals_float]
    err_floatnum = [approx for _,_,approx,_ in pivals_floatnum]

    t_fixedpr = [approx for _,_,_,approx in pivals_fixedpr]
    t_decimal= [approx for _,_,_,approx in pivals_decimal]
    t_float = [approx for _,_,_,approx in pivals_float]
    t_floatnum = [approx for _,_,_,approx in pivals_floatnum]

    fig, axs = plt.subplots(nrows=1,ncols=3, figsize=(12, 4))

    axs[0].plot(numterm, p_float, marker='o')
    axs[0].axhline(y=np.pi, color='r', linestyle='--', label=r'$\pi_{numpy}$')
    axs[0].set_xlabel('Number of digits')
    axs[0].set_ylabel(r'Approximation of $\pi$')
    axs[0].set_title(r'Approximating $\pi$ using Gauss-Legendre algorithm')
    axs[0].legend()
    axs[0].set_xscale('log', base=10)

    axs[1].plot(numterm, err_float, marker='o', label='float')
    axs[1].plot(numterm, err_floatnum, marker='o', label='FloatNumber')
    axs[1].plot(numterm, err_fixedpr, marker='o', label='FixedPrecision')
    axs[1].plot(numterm, err_decimal, marker='o', label='Decimal')
    axs[1].set_xlabel('Number of digits')
    axs[1].set_ylabel(r'$|\pi_{approx} -\pi_{numpy}|$')
    axs[1].set_title(f'Error of the Approximation with precision {outputprec}')
    axs[1].legend()
    axs[1].set_xscale('log', base=10)
    axs[1].set_yscale('log', base=10)


    axs[2].plot(numterm, t_float, marker='o', label='float')
    axs[2].plot(numterm, t_floatnum, marker='o', label='FloatNumber')
    axs[2].plot(numterm, t_fixedpr, marker='o', label='FixedPrecision')
    axs[2].plot(numterm, t_decimal, marker='o', label='Decimal')
    axs[2].set_xlabel('Number of digits')
    axs[2].set_ylabel(r'$\Delta t$')
    axs[2].set_title(r'Runtime of the Approximation')
    axs[2].legend()
    axs[2].set_xscale('log', base=10)
    axs[2].set_yscale('log', base=10)

    fig.tight_layout()
    plt.show()



