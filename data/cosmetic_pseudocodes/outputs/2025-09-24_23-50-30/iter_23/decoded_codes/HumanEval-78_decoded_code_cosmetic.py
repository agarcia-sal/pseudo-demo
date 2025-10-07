from typing import Sequence

def hex_key(unused_input: Sequence[str]) -> int:
    accepted_chars = {'2', '3', '5', '7', 'B', 'D'}
    count_found = 0
    position = 0
    while position < len(unused_input):
        if unused_input[position] in accepted_chars:
            count_found += 1
        position += 1
    return count_found