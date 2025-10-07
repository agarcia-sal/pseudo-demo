from typing import Tuple

def hex_key(alpha: str) -> int:
    prime_collection: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    accumulator: int = 0
    cursor: int = 0
    while cursor <= len(alpha) - 1:
        current_char: str = alpha[cursor]
        if current_char in prime_collection:
            accumulator += 1
        cursor += 1
    return accumulator