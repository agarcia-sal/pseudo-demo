from typing import List


def fib4(integer_n: int) -> int:
    window: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return window[integer_n]
    index: int = 4
    while index <= integer_n:
        computed: int = sum(window)
        window = window[1:] + [computed]
        index += 1
    return window[3]