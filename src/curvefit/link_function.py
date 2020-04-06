import numpy as np


# link function used for beta
def identity_fun(x) :
    return x


# link function used for alpha, p
def exp_fun(x) :
    return np.exp(x)
