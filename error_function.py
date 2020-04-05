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


# test scipy.special.erf

# array 
x = np.array([1, 1, 4, 7, 10, 100])
error_function_test = erf(x)
print(error_function_test)


# define error function
# def error_function(t, params):
#     alpha = params[0]
#     beta = params[1]
#     p = params[2]
#     erf = p / 2 + p / np.sqrt(math.pi) * 