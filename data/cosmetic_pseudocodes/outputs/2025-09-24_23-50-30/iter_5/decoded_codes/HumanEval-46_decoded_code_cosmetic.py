from typing import List


def fib4(integer_n: int) -> int:
    cache: List[int] = [0, 0, 2, 0]

    if integer_n >= 4:
        index = 4
        while index <= integer_n:
            sum_four = sum(cache)
            cache = cache[1:] + [sum_four]
            index += 1
        return cache[3]
    else:
        return cache[integer_n]