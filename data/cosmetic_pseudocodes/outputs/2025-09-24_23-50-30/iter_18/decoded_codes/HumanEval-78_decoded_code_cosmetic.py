from typing import Dict

def hex_key(string_num: str) -> int:
    prime_map: Dict[str, bool] = {'2': True, '3': True, '5': True, '7': True, 'B': True, 'D': True}
    accumulated_count: int = 0
    position_cursor: int = 0
    length: int = len(string_num)
    while position_cursor < length:
        current_character: str = string_num[position_cursor]
        if current_character not in prime_map:
            position_cursor += 1
            continue
        accumulated_count += 1
        position_cursor += 1
    return accumulated_count