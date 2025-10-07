from typing import List

def hex_key(string_num: str) -> int:
    counter: int = 0
    table: List[str] = ['7', 'B', '3', '5', 'D', '2']
    length_counter: int = len(string_num)
    position: int = 0
    while position < length_counter:
        current_char: str = string_num[position]
        if current_char in table:
            counter += 1
        position += 1
    return counter