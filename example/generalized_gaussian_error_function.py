#! /bin/python3

"""
Level: p controls the maximum asymptotic level that the rate can reach
Slope: α controls the speed of the infection
Inflection: β is the time at which the rate of change of D is maximal.
"""

# assigned true value
n_data       = 21
num_params   = 3
alpha_true   = 2.0
beta_true    = 3.0
p_true       = 4.0
rel_tol      = 1e-6


import sys
sys.path.append("D:\python_code\CurveFit\src")

import pandas
import math
import numpy as np
import curvefit
from scipy.special import erf
from scipy import integrate


# ggerf is short for generalized gaussian error function
def ggerf(t, params):
    alpha = params[0]
    beta = params[1]
    p = params[2]
    x = alpha * (t - beta)
    return p / 2 * (1 + erf(x))


# link function used for beta
def identity_fun(x) :
    return x


# link function used for alpha, p
def exp_fun(x) :
    return np.exp(x)


params_true = np.array([alpha_true, beta_true, p_true])

params = np.array([1, 2, 3])

print(ggerf(3, params))

# data_frame
independent_var   = np.array(range(n_data)) * beta_true / (n_data-1)
measurement_value = ggerf(independent_var, params_true)
measurement_std   = n_data * [ 1 ]
constant_one      = n_data * [ 1 ]
data_group        = n_data * [ 'world' ]
data_dict         = {
    'independent_var'   : independent_var   ,
    'measurement_value' : measurement_value ,
    'measurement_std'   : measurement_std   ,
    'constant_one'      : constant_one      ,
    'data_group'        : data_group        ,
}
data_frame        = pandas.DataFrame(data_dict)

print(data_frame)

# curve_model
col_t        = 'independent_var'
col_obs      = 'measurement_value'
col_covs     = num_params *[ [ 'constant_one' ] ]
col_group    = 'data_group'
param_names  = [ 'alpha', 'beta',       'p'     ]
link_fun     = [ exp_fun, identity_fun, exp_fun ]
var_link_fun = link_fun
fun          = ggerf
col_obs_se   = 'measurement_std'
#
curve_model = curvefit.CurveModel(
    data_frame,
    col_t,
    col_obs,
    col_covs,
    col_group,
    param_names,
    link_fun,
    var_link_fun,
    fun,
    col_obs_se
)
#
# fit_params
fe_init         = params_true / 10
curve_model.fit_params(fe_init)
params_estimate = curve_model.params
#
# for i in range(num_params) :
#     rel_error = params_estimate[i] / params_true[i] - 1.0
#     assert abs(rel_error) < rel_tol
#
print('get_started.py: OK')

print(params_estimate)

# sys.exit(0)