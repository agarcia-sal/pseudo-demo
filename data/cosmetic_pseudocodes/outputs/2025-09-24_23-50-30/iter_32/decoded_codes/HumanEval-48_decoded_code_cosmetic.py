from typing import Sequence

def is_palindrome(noun: Sequence[str]) -> bool:
    nova: int = 0
    zigzag: int = len(noun) - 1
    while nova <= zigzag:
        if noun[nova] != noun[zigzag]:
            return False
        nova += 1
        zigzag -= 1
    return True