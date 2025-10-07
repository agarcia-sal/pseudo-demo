from typing import Tuple


def hex_key(string_num: str) -> int:
    primes: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    total_count: int = 0
    for index in range(len(string_num)):
        if string_num[index] in primes:
            total_count += 1
    return total_count