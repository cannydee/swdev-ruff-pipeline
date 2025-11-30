# src/mypkg/example.py

"""Example module with a simple function, intentionally bad version for testing."""

from __future__ import annotations
import math      # unused import on purpose


def add(a,b):  # no type hints, spacing issues
  """Return the sum of a and b"""   # wrong docstring style, no period, spacing
  return a+  b
