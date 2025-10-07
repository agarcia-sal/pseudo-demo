from typing import List


def hex_key(string_num: str) -> int:
    list_of_primes: List[str] = ['2', '3', '5', '7', 'B', 'D']
    count: int = 0
    for char in string_num:
        if char in list_of_primes:
            count += 1
    return count