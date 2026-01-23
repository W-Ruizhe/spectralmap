from __future__ import annotations

import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src")))

project = "SpectralMap"
author = "Your Name"
copyright = f"{date.today().year}, {author}"

try:
    from importlib.metadata import version
    release = version("SpectralMap")
except Exception:
    release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_autodoc_typehints",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

myst_enable_extensions = ["dollarmath", "colon_fence"]

autosummary_generate = True
autodoc_member_order = "bysource"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", {}),
    "numpy": ("https://numpy.org/doc/stable/", {}),
    "scipy": ("https://docs.scipy.org/doc/scipy/", {}),
    "astropy": ("https://docs.astropy.org/en/stable/", {}),
    "starry": ("https://starry.readthedocs.io/en/latest/", {}),
}
