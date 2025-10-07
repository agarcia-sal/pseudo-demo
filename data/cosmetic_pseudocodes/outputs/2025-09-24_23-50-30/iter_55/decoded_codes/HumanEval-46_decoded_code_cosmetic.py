from typing import Tuple

def fib4(integer_x: int) -> int:
    buffer = [0, 0, 2, 0]

    def helper(current_i: int, limit_i: int, window: Tuple[int, int, int, int]) -> int:
        if current_i > limit_i:
            return window[3]
        sum_val = sum(window)
        new_window = (window[1], window[2], window[3], sum_val)
        return helper(current_i + 1, limit_i, new_window)

    if integer_x < 4:
        return buffer[integer_x]
    return helper(4, integer_x, tuple(buffer))