Tutorial 3: Bayesian retrieval workflow (skeleton)
==================================================

Goal
----

Turn the inversion into a Bayesian model.

Common pattern
--------------

- Likelihood: Gaussian (or Student-t)
- Priors: smoothness / positivity / physical constraints
- Inference: HMC/NUTS, VI, nested sampling

Checklist
---------

- Define parameters + constraints.
- Add forward model (rotation + eclipse).
- Validate on simulations (posterior predictive checks).
- Apply to real data with systematics control.
