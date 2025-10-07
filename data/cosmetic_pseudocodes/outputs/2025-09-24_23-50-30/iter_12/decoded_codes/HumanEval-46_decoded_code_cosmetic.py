from typing import List

def fib4(integer_n: int) -> int:
    def helper(current_index: int, window_list: List[int]) -> int:
        if current_index > integer_n:
            return window_list[3]

        sum_four = sum(window_list)  # sum of the 4 elements in window_list
        new_window = [window_list[1], window_list[2], window_list[3], sum_four]

        return helper(current_index + 1, new_window)

    initial_window: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return initial_window[integer_n]

    return helper(4, initial_window)