from typing import Callable

def fib(v_001: int) -> int:
    def helper(v_002: int, v_003: int, v_004: int) -> int:
        if v_002 == 0:
            return v_003
        if v_002 > 0:
            return helper(v_002 - 1, v_004, v_003 + v_004)
        # If v_002 < 0: no explicit behavior defined; assume no call in that case
        raise ValueError("v_002 must be non-negative")
    return helper(v_001, 0, 1)