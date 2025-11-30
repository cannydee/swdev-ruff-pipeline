# src/mypkg/example.py

"""Example math helper functions for the docs exercise."""

from __future__ import annotations


def add(a: int, b: int) -> int:
    """
    Add two integers.

    Parameters
    ----------
    a:
        First integer.
    b:
        Second integer.

    Returns
    -------
    int
        Sum of the two inputs.
    """
    return a + b


def mean(values: list[float]) -> float:
    """
    Compute the arithmetic mean of a list of numbers.

    Parameters
    ----------
    values:
        Non-empty list of numeric values.

    Returns
    -------
    float
        Arithmetic mean of the given values.

    Raises
    ------
    ValueError
        If `values` is empty.
    """
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)
