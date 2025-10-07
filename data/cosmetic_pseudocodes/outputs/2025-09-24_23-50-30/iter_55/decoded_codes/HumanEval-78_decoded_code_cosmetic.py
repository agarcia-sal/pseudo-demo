from typing import Set

def hex_key(alpha: str) -> int:
    prime_collection: Set[str] = {'2', '3', '5', '7', 'B', 'D'}
    accumulator: int = 0
    cursor: int = 0
    while cursor < len(alpha):
        if alpha[cursor] in prime_collection:
            accumulator += 1
        cursor += 1
    return accumulator