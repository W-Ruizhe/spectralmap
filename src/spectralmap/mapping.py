"""Core mapping stubs.

Replace these with your real forward/inference code.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np

@dataclass
class LightCurveData:
    """Container for light curve (or spectrophotometric) time series."""
    time: np.ndarray
    flux: np.ndarray
    flux_err: np.ndarray | None = None
    wavelength: np.ndarray | None = None  # optional: wavelength bins

def simulate_placeholder(time: np.ndarray, period: float = 5.0, amp: float = 0.01) -> np.ndarray:
    """A tiny placeholder simulator (sine wave)."""
    return 1.0 + amp * np.sin(2*np.pi*time/period)
