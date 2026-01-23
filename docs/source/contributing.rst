Contributing
============

Local dev
---------

.. code-block:: bash

   pip install -e ".[dev,docs]"
   pytest
   ruff check .

Docs
----

.. code-block:: bash

   cd docs
   make html
