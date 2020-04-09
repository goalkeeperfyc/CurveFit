# Implement Notes

## Important Info

- Target: cumulative death rate / population. It's extensionable.
- Not well documented. The example is to create `independent_var`.
- We don't miss any death cases. But for testing positive cases, we may miss some.
- For SIR model, S is unknown, I has a huge error at the beginning because test capacity can't cover all patients.
- Other advanced model: MSEIRS, MSEIR.
- We only have four factors SEIR


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
