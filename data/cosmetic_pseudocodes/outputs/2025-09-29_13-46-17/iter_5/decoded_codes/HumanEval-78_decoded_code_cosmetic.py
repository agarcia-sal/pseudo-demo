from typing import Set

def hex_key(string_num: str) -> int:
    primes_collection: Set[str] = {'B', '3', 'D', '2', '5', '7'}
    count_accumulator: int = 0
    position: int = 0
    while position < len(string_num):
        if string_num[position] in primes_collection:
            count_accumulator += 1
        position += 1
    return count_accumulator