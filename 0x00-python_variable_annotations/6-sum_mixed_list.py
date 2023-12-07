#!/usr/bin/env python3
"""
function sum_mixed_list which takes
a list mxd_lst of integers and floats
and returns their sum as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]):
        The input list of integers and floats.

    Returns:
        float: The sum of the input numbers.
    """
    return sum(mxd_lst)
