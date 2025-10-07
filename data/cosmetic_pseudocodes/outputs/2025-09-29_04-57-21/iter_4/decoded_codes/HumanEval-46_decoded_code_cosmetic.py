from typing import List


def fib4(integer_n: int) -> int:
    window: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return window[integer_n]

    current_index: int = 4
    while current_index <= integer_n:
        computed_sum = sum(window)
        window.append(computed_sum)
        window.pop(0)  # remove the oldest element to keep window size 4
        current_index += 1

    return window[-1]