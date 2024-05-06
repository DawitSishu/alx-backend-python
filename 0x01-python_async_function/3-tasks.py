#!/usr/bin/env python3
""" async """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ tasks create them """
    task = create_task(wait_random(max_delay))
    return task
