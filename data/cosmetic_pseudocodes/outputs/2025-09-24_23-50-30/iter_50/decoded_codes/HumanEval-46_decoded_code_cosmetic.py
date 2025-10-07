from typing import List


def fib4(integer_n: int) -> int:
    cache_list: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return cache_list[integer_n]
    loop_index: int = 4
    while loop_index <= integer_n:
        sum_next = sum(cache_list)
        cache_list.append(sum_next)
        cache_list.pop(0)
        loop_index += 1
    return cache_list[3]