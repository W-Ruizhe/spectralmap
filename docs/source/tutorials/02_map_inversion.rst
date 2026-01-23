Tutorial 2: Deterministic map inversion (skeleton)
==================================================

Goal
----

Set up a deterministic inversion:

.. math::

   y \approx f(\theta), \qquad
   \hat\theta = \arg\min_\theta \|y - f(\theta)\|^2 + \lambda R(\theta).

Template steps
--------------

1. Choose parameterization
   - Spherical harmonics
   - Pixel map / HEALPix
   - Low-rank basis (PCA / eigencurves)

2. Choose regularization
   - L2 / smoothness
   - sparsity
   - physical constraints

3. Implement forward model
   - rotation-only
   - eclipse/occultation geometry
   - multi-wavelength extension
