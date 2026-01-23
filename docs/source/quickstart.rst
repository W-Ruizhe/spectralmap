Quickstart
==========

1. Simulate a toy light curve
-----------------------------

.. code-block:: python

   import numpy as np
   from spectralmap.mapping import simulate_placeholder

   t = np.linspace(0, 10, 500)
   f = simulate_placeholder(t, period=5.0, amp=0.01)

2. Where to put your code
-------------------------

- Core algorithms in ``src/spectralmap/``.
- Tutorials in ``docs/source/tutorials/``.
