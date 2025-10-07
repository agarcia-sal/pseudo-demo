from typing import Sequence

def hex_key(alpha_beta: Sequence[str]) -> int:
    prime_collection = {'2', '3', '5', '7', 'B', 'D'}  # Use set for O(1) membership tests
    accumulated_count = 0
    cursor = 0
    while cursor < len(alpha_beta):
        if alpha_beta[cursor] in prime_collection:
            accumulated_count += 1
        cursor += 1
    return accumulated_count