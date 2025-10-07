from typing import List


def fib4(integer_n: int) -> int:
    window_elements: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return window_elements[integer_n]

    index: int = 4
    while index <= integer_n:
        computed_sum: int = sum(window_elements)
        window_elements.pop(0)
        window_elements.append(computed_sum)
        index += 1

    return window_elements[3]