from typing import Sequence

def hex_key(input_sequence: Sequence[str]) -> int:
    prime_collection = {'D', '3', '2', 'B', '7', '5'}
    prime_counter = 0
    cursor = 0
    while cursor < len(input_sequence):
        if input_sequence[cursor] in prime_collection:
            prime_counter += 1
        cursor += 1
    return prime_counter