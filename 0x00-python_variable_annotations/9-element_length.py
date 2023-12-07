#!/usr/bin/env python3
"""
Annotated the function below for the
paremeters to return values with
the appropriate type
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple
    contains an element from the input list
    and its corresponding length.

    Args:
        lst (Iterable[Sequence]):
        The input iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        where each tuple contains an element
        from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
