#!/usr/bin/env python3
"""
Use mypy to validate the
following piece of code and
apply any necessary changes.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

"""
The correct usage should be an integer as the factor
"""


zoom_3x = zoom_array(array, 3)

"""
You can also omit the type annotations
in the call, mypy will infer them
"""


zoom_4x = zoom_array(array, 4)
