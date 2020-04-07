#! /bin/python3
# vim: set expandtab:
# -------------------------------------------------------------------------

# Level: p controls the maximum asymptotic level that the rate can reach
# Slope: α controls the speed of the infection
# Inflection: β is the time at which the rate of change of D is maximal.

import sys
import os
import pandas as pd
import numpy as np
import random 
# add path to sys path
sys.path.append("D:\python_code\CurveFit\src")
import curvefit
from curvefit.glm_function import generalized_gaussian_error_function
from curvefit.link_function import exp_fun, identity_fun


df = pd.read_csv(os.getcwd() + "/implement/data/Italy_death_rate.csv")
df = df.loc[df["day"] > 0, ]

# curve_model
col_t = 'day'
col_obs = 'cdr'
col_covs = 3 * [['constant_one']]
col_group = 'country'
param_names = ['alpha','beta','p']
link_fun = [exp_fun, identity_fun, exp_fun]
var_link_fun = link_fun
fun = generalized_gaussian_error_function
col_obs_se = 'std'
#
curve_model = curvefit.CurveModel(
    df,
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
fe_init = np.array([0.5, 20, 0.2])
# print(fe_init)
curve_model.fit_params(fe_init)
params_estimate = curve_model.params
#
# for i in range(num_params) :
#     rel_error = params_estimate[i] / params_true[i] - 1.0
#     assert abs(rel_error) < rel_tol
#
# print('get_started.py: OK')

print(params_estimate)

# sys.exit(0)

t = generalized_gaussian_error_function(df["cdr"], params_estimate)

print(str(t))