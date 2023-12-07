#!/usr/bin/env python3
"""
function sum_list which takes a list
input_list of floats as arguments and
returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): The input list of floating-point numbers.

    Returns:
        float: The sum of the input numbers.
    """
    return sum(input_list)
