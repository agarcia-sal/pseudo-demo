from collections import deque
from functools import reduce
from typing import Deque


def fizz_buzz(n: int) -> int:
    multiples_collection: Deque[int] = deque()

    def collect_multiples(index: int) -> None:
        if index < n:
            if not (index % 11 != 0 and index % 13 != 0):
                multiples_collection.append(index)
            collect_multiples(index + 1)

    collect_multiples(0)

    concat_str: str = reduce(lambda acc, val: acc + str(val), multiples_collection, "")

    seven_counter: int = 0
    for position in range(1, len(concat_str) + 1):
        if concat_str[position - 1] == '7':
            seven_counter += 1

    return seven_counter