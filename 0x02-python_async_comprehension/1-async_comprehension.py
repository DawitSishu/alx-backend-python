#!/usr/bin/env python3
""" number module """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    function to return 10 numbers
    """
    r = [i async for i in async_generator()]
    return r
