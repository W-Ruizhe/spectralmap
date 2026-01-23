Read the Docs setup (step-by-step)
==================================

Prerequisites
-------------

- A GitHub repo containing this project
- The Sphinx docs folder (already included: ``docs/``)
- A Read the Docs config at repo root: ``.readthedocs.yaml``

Step 1 — Build docs locally
---------------------------

.. code-block:: bash

   pip install -e ".[docs]"
   sphinx-build -b html docs/source docs/_build/html
   open docs/_build/html/index.html

Step 2 — Push to GitHub
-----------------------

Commit everything (including ``docs/`` and ``.readthedocs.yaml``), then push to GitHub.

Step 3 — Import into Read the Docs
----------------------------------

1. Log in to Read the Docs.
2. “Import a project” and select your GitHub repo.
3. Read the Docs should detect ``.readthedocs.yaml`` automatically.

Step 4 — Trigger a build & fix build log errors
-----------------------------------------------

- Push a new commit (or click “Build version”).
- If you see import errors, ensure your package is installed via the
  ``python.install`` section in ``.readthedocs.yaml`` (this template already does that).

Common issues
-------------

- **autodoc import errors**: your package isn’t installed in the RTD build environment.
- **missing theme**: add ``sphinx-rtd-theme`` to docs requirements.
- **no API pages**: ensure modules are listed in ``api.rst`` and importable.
