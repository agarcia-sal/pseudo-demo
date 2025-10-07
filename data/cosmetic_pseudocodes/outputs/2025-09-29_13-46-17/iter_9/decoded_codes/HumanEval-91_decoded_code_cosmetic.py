import re
from typing import Callable

def is_bored(input_string: str) -> int:
    scanner: Callable[[str, str], list[str]] = re.split
    Ωψπξχλ: int = 0
    Ϟ₰𝄞: list[str] = scanner(r'[.?!]\s*', input_string)

    def recursive_check(INDEX: int, ACCUMULATOR: int) -> int:
        if INDEX == len(Ϟ₰𝄞):
            return ACCUMULATOR
        else:
            segment = Ϟ₰𝄞[INDEX]
            # Check if the segment starts with 'I '
            if not ((segment[:2] == 'I ' ) is False):
                return recursive_check(INDEX + 1, ACCUMULATOR + 1)
            else:
                return recursive_check(INDEX + 1, ACCUMULATOR)

    Ψλκμ₄₇: int = recursive_check(0, Ωψπξχλ)
    return Ψλκμ₄₇