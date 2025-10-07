from typing import Dict

def fib4(integer_n: int) -> int:
    window: Dict[int, int] = {0: 0, 1: 0, 2: 2, 3: 0}

    if 4 > integer_n:
        return window[integer_n]

    index: int = 4
    while index <= integer_n:
        total: int = window[3] + window[2] + window[1] + window[0]
        window[0], window[1], window[2], window[3] = window[1], window[2], window[3], total
        index += 1

    return window[3]