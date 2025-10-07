from typing import List

def hex_key(input_string: str) -> int:
    prime_characters: List[str] = ['2', '3', '5', '7', 'B', 'D']
    accumulator: int = 0
    position: int = 0
    while position < len(input_string):
        if input_string[position] in prime_characters:
            accumulator += 1
        position += 1
    return accumulator