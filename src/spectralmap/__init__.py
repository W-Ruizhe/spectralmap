"""SpectralMap: rotational + eclipse mapping toolkit (template).

A starting point for:
- rotational modulation mapping (phase curves, spot/cloud inference)
- eclipse / occultation mapping (ingress/egress constraints)
- wavelength-resolved ("spectral") mapping workflows
"""

from importlib.metadata import version as _version

__all__ = ["__version__"]
__version__ = _version("SpectralMap")
