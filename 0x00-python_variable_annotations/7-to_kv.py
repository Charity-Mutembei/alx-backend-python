#!/usr/bin/env python3
"""
function to_kv that takes a string k and
an int OR float v as an argument and
returns a tuple.
The first element is the string k, the second
element is the square of the int/float v and
should be annotated as a float
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with the string k as
    the first element and the square of the int/float v
    as the second element.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input integer or float.

    Returns:
        Tuple[str, float]: A tuple with the
        input string and the square of the input number.
    """
    return (k, v**2)
