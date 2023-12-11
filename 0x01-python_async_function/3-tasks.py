#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax.
Write a function (do not create an async function,
use the regular function syntax to do this)
task_wait_random that takes an integer max_delay and
returns a asyncio.Task.
"""

import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that returns an asyncio.Task for wait_random.

    Parameters:
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - asyncio.Task: The asyncio task for wait_random.
    """
    coroutine = wait_random(max_delay)
    task = asyncio.create_task(coroutine)
    return task
