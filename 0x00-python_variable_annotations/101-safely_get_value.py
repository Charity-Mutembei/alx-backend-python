#!/usr/bin/env python3
"""
parameters and return values, add
type annotations to the function
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any, default: Union[T,
                                              None] = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to retrieve the value.
        default (Union[T, None], optional):
        The default value if the key is not present. Defaults to None.

    Returns:
        Union[Any, T]:
        The value associated with the key or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
