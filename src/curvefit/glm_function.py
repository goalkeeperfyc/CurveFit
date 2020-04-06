#! /bin/python3


"""
some generalized linear models are here.
"""


import math
import numpy as np
from scipy.special import erf


def generalized_gaussian_error_function(t, params):
    alpha = params[0]
    beta = params[1]
    p = params[2]
    x = alpha * (t - beta)
    return p / 2 * (1 + erf(x))


def generalized_logistic(t, params) :
    alpha = params[0]
    beta = params[1]
    p = params[2]
    x = - alpha * (t - beta)
    return p / (1 + math.exp(x))
