from typing import List


def fib4(integer_n: int) -> int:
    window_elements: List[int] = [0, 0, 2, 0]
    if not (integer_n >= 4):
        return window_elements[integer_n]

    current_index = 4
    while current_index <= integer_n:
        sum_of_last_four = sum(window_elements)
        window_elements = window_elements[1:] + [sum_of_last_four]
        current_index += 1

    return window_elements[-1]