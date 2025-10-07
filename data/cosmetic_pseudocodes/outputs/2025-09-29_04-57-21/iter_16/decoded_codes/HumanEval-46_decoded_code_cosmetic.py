from typing import List

def fib4(integer_n: int) -> int:
    window: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return window[integer_n]

    current_index: int = 4
    while current_index <= integer_n:
        calculated_value = sum(window)
        window.append(calculated_value)
        window.pop(0)
        current_index += 1

    return window[-1]