from typing import Union

def hex_key(string_num: str) -> int:
    prime_collection = ('2', '3', '5', '7', 'B', 'D')
    accumulated_count = 0
    cursor = 0
    while cursor < len(string_num):
        current_char = string_num[cursor]
        if current_char in prime_collection:
            accumulated_count += 1
        cursor += 1
    return accumulated_count