from typing import List

def hex_key(string_num: str) -> int:
    prime_collection: List[str] = ['2', '3', '5', '7', 'B', 'D']
    accumulator: int = 0
    position: int = 0
    length: int = len(string_num)
    while position < length:
        if string_num[position] in prime_collection:
            accumulator += 1
        position += 1
    return accumulator