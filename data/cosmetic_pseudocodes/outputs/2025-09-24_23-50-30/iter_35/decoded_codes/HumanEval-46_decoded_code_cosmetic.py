from typing import List

def fib4(integer_n: int) -> int:
    window: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return window[integer_n]

    index: int = 4
    while index <= integer_n:
        next_term: int = sum(window)
        window = [window[1], window[2], window[3], next_term]
        index += 1

    return window[3]