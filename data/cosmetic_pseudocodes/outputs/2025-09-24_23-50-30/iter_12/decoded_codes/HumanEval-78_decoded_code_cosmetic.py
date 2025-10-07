from typing import List


def hex_key(string_num: str) -> int:
    primes_collection: List[str] = ['2', '3', '5', '7', 'B', 'D']
    accumulator: int = 0
    position: int = 0

    while position < len(string_num):
        if string_num[position] in primes_collection:
            accumulator += 1
        position += 1

    return accumulator