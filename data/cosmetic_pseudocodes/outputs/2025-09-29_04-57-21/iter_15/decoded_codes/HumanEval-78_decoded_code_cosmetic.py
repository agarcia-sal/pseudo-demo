from typing import Sequence

def hex_key(string_num: str) -> int:
    prime_collection: set[str] = {'2', '3', '5', '7', 'B', 'D'}
    accumulator: int = 0
    pos: int = 0
    while pos < len(string_num):
        if string_num[pos] in prime_collection:
            accumulator += 1
        pos += 1
    return accumulator