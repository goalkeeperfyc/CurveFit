# Implement Notes

## Understand Parameters

- [x] col_t: independent variable (`time t`).
- [x] col_obs: response variable (`log of cumulative death rate`)
- [x] col_covs: list of list of column name in the data frame used as covariates. (`num_params * [['constant_one']]`)
- [x] col_group: which group does this row belong to.
- [x] param_names: `alpha, beta, p`.
- [x] link_fun: link functions for $\alpha, \beta$ and `p`, which are `exp_fun, identity_fun, exp_fun`.
- [x] var_link_fun: link functions for variables including fixed effects and random effects. Same as `link_func`.
- [x] fun: the function we used (`generalized gaussian error function`)
- [x] col_obs_se: The standand deviation of response variable. The effect is unknown.

## Implement Data From

- Italy
- Spain
- US
- New York
- Florida
