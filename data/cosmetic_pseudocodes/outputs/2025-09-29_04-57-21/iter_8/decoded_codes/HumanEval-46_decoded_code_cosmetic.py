from typing import List

def fib4(integer_n: int) -> int:
    window: List[int] = [0, 0, 2, 0]  # initial sequence values

    if integer_n < 4:
        return window[integer_n]

    count: int = 4
    while count <= integer_n:
        total: int = sum(window)  # sum of last four values
        window.append(total)
        window.pop(0)  # remove oldest value to maintain window size 4
        count += 1

    return window[-1]