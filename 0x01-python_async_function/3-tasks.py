#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax.
Write a function (do not create an async function,
use the regular function syntax to do this)
task_wait_random that takes an integer max_delay and
returns a asyncio.Task.
"""

import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Callable:
    """
    Regular function that returns an asyncio.Task.

    Parameters:
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - Callable: A function that, when called, returns an asyncio.Task.
    """
    async def wait_random_wrapper():
        return await wait_random(max_delay)

    return asyncio.create_task(wait_random_wrapper())
