from typing import Tuple

def hex_key(string_num: str) -> int:
    prime_chars: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    count: int = 0
    for char in string_num:
        if char in prime_chars:
            count += 1
    return count