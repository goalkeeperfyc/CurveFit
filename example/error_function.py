#! /bin/python3

"""
Level: p controls the maximum asymptotic level that the rate can reach
Slope: α controls the speed of the infection
Inflection: β is the time at which the rate of change of D is maximal.
"""

import sys
sys.path.append("D:\python_code\CurveFit\src")

import pandas
import math
import numpy as np
import curvefit
from scipy.special import erf
from scipy import integrate

# test scipy.special.erf

# array 
x = np.array([x/100 for x in range(1, 11)])
# x = np.array([1, 1, 4, 7, 10, 100])
# error_function_test = erf(x)
# print(x)
# print(erf(x))


# define error function
# def error_function(t, params):
#     alpha = params[0]
#     beta = params[1]
#     p = params[2]
#     erf = p / 2 + p / np.sqrt(math.pi) * 


def error_function(x):
    return 2 / math.sqrt(math.pi) * math.exp(-x**2)


# assert error_function(2) == 2 / math.pi * np.exp(-4)

# print(error_function(2))
# print(np.exp(-4))

i, error = integrate.quad(error_function, 0, 0.1)
# print(i)
# print(erf(0.1))

t = 3
params = np.array([1, 2, 3])
alpha = params[0]
beta = params[1]
p = params[2]
x = alpha * (t - beta)

print(erf(x))