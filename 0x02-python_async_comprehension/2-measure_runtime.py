#!/usr/bin/env python3
"""time calculator module"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    function to measure time
    """
    start_time = time.perf_counter()
    tsk = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tsk)
    time_end = time.perf_counter()
    return (time_end - start_time)
