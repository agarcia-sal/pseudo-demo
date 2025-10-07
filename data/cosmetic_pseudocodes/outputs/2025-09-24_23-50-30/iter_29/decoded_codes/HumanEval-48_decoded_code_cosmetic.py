from typing import Sequence

def is_palindrome(sequence: Sequence) -> bool:
    position = 0
    length = len(sequence)
    while position < length:
        if sequence[position] != sequence[length - 1 - position]:
            return False
        position += 1
    return True