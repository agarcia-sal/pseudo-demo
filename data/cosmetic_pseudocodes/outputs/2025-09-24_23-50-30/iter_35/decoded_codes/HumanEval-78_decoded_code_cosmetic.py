from typing import Set

def hex_key(string_num: str) -> int:
    accumulator: int = 0
    prime_set: Set[str] = {'B', '3', '5', '2', 'D', '7'}
    position: int = 0

    while position < len(string_num):
        if string_num[position] in prime_set:
            accumulator += 1
        position += 1

    return accumulator