from typing import List

def fib4(integer_n: int) -> int:
    cache: List[int] = [0, 0, 2, 0]
    if integer_n <= 3:
        return cache[integer_n]

    index = 4
    while index <= integer_n:
        tally = sum(cache)
        cache.pop(0)
        cache.append(tally)
        index += 1

    return cache[3]