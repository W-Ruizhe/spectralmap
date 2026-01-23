Tutorial 1: Simulating rotational modulation
============================================

Goal
----

Generate a simple synthetic light curve and define the data model you’ll reuse everywhere.

Steps
-----

1. Create a time grid and a toy signal.

.. code-block:: python

   import numpy as np
   from spectralmap.mapping import simulate_placeholder

   t = np.linspace(0, 10, 1000)
   f = simulate_placeholder(t, period=5.0, amp=0.01)

2. Add noise.

.. code-block:: python

   rng = np.random.default_rng(0)
   sigma = 5e-4
   y = f + rng.normal(0, sigma, size=f.size)
