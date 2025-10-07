from typing import List

def hex_key(alpha: str) -> int:
    prime_chars: List[str] = ['2', '3', '5', '7', 'B', 'D']
    count: int = 0
    pos: int = 0
    while pos < len(alpha):
        if alpha[pos] in prime_chars:
            count += 1
        pos += 1
    return count