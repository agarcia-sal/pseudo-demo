from typing import List

def fib4(integer_n: int) -> int:
    sliding_window: List[int] = [0, 0, 2, 0]

    if integer_n >= 4:
        def helper(current_index: int, window: List[int]) -> int:
            if current_index > integer_n:
                return window[3]
            new_element = sum(window)
            return helper(current_index + 1, [window[1], window[2], window[3], new_element])

        return helper(4, sliding_window)
    return sliding_window[integer_n]