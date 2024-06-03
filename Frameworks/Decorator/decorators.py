"""
Heavily based on the workflow and video by anthonywritescode (asotille on GitHub)
https://www.youtube.com/watch?v=_QXlbwRmqgI
"""

import contextlib
import time
from typing import Generator

# TODO: Import logger here
# TODO: Optional: Import global configs

# TODO: Create/Assign Logger here
# TODO: Replace print() calls with logger calls

@contextlib.contextmanager
def example_timing_ctx(name: str=None) -> Generator[None, None, None]:
    t0 = time.monotonic()
    try:
        yield
    finally:
        t1 = time.monotonic()
        print(f"LOG: {name} took: {round(t1 - t0, 3)}s")
