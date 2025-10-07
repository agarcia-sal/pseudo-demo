from typing import Callable

def add(x: int, y: int) -> int:
    def _accumulate(lhs_val: int, rhs_val: int) -> int:
        matched_result = lhs_val
        if rhs_val == 0:
            return matched_result
        else:
            return _accumulate(matched_result + 1, rhs_val - 1)
    return _accumulate(x, y)