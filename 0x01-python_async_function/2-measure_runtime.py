#!/usr/bin/env python3
"""
Create a measure_time function with integers n
and max_delay as arguments that measures the
total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.
Use the time module to measure an approximate elapsed time.
"""

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Parameters:
    - n (int): The number of times to spawn wait_random.
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - float: The average time per execution.
    """
    async def run_wait_n():
        await wait_n(n, max_delay)

    start_time = time.time()
    asyncio.run(run_wait_n())
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
