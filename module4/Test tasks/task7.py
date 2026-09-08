from typing import Dict

import time

execution_time: Dict[str, float] = {}


def time_decorator(fn):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = fn(*args, **kwargs)

        end = time.time()

        execution_time[fn.__name__] = end - start

        return result
    return wrapper
