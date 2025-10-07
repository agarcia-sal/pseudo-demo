from typing import List


def fib4(integer_n: int) -> int:
    cache: List[int] = [0, 0, 2, 0]

    if not (integer_n >= 4):
        return cache[integer_n]

    counter: int = 4
    while counter <= integer_n:
        accumulator: int = sum(cache)
        cache.append(accumulator)
        cache.pop(0)
        counter += 1

    return cache[-1]