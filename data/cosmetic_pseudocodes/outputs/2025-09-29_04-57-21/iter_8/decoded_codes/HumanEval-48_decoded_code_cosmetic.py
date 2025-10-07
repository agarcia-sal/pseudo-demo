from typing import Sequence

def is_palindrome(content: Sequence[str]) -> bool:
    position: int = 0
    upper_bound: int = len(content) - 1

    while position <= upper_bound:
        front_char: str = content[position]
        back_char: str = content[upper_bound - position]

        if front_char != back_char:
            return False

        position += 1

    return True