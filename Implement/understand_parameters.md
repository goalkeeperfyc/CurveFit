# Understand Parameters

- [x] col_t: independent variable (`time t`).
- [x] col_obs: response variable (`log of cumulative death rate`)
- [ ] col_covs: ?     = num_params *[ [ 'constant_one' ] ]
- [x] col_group: which group does this row belong to.
- [x] param_names: `alpha, beta, p`.
- [x] link_fun: link function for $\alpha, \beta$ and `p`, which are `exp_fun, identity_fun, exp_fun`.
- [ ] var_link_fun: link function for variables including fixed effects and random effects.
- [x] fun: the function we used (`generalized gaussian error function`)
- [ ] col_obs_se: The standand deviation of response variable. The effect is unknown.
