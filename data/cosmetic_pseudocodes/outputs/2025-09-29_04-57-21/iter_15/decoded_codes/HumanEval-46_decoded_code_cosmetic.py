from typing import List

def fib4(integer_n: int) -> int:
    sliding_window: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return sliding_window[integer_n]

    current_index: int = 4
    while current_index <= integer_n:
        aggregated_sum: int = sum(sliding_window)
        sliding_window.append(aggregated_sum)
        sliding_window.pop(0)
        current_index += 1

    return sliding_window[-1]