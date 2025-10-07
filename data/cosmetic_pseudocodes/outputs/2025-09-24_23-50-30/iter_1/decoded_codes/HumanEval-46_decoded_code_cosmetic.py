from typing import List

def fib4(integer_n: int) -> int:
    window: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return window[integer_n]

    counter: int = 4
    while counter <= integer_n:
        sum_four = sum(window)
        window = window[1:4]
        window.append(sum_four)
        counter += 1

    return window[3]