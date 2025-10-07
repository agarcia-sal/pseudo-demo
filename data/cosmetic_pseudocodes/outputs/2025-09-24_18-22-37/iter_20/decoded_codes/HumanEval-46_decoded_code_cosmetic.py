from typing import List


def fib4(delta: int) -> int:
    cache: List[int] = [0, 0, 2, 0]

    if delta < 4:
        return cache[delta]

    counter: int = 4
    while counter <= delta:
        partial_sum_first: int = cache[0] + cache[1]
        partial_sum_second: int = cache[2] + cache[3]
        next_candidate: int = partial_sum_first + partial_sum_second

        cache.append(next_candidate)
        cache.pop(0)
        counter += 1

    final_output: int = cache[3]
    return final_output