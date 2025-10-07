from typing import List

def fib4(integer_n: int) -> int:
    result_set: dict[int, int] = {0: 0, 1: 0, 2: 2, 3: 0}

    def helper_f(curr_index: int, window_list: List[int]) -> int:
        if curr_index > integer_n:
            return window_list[3]
        sum_four = window_list[0] + window_list[1] + window_list[2] + window_list[3]
        shifted_window = [window_list[1], window_list[2], window_list[3], sum_four]
        return helper_f(curr_index + 1, shifted_window)

    guard_condition = integer_n >= 4
    return (helper_f(4, [0, 0, 2, 0]) if guard_condition else result_set[integer_n])