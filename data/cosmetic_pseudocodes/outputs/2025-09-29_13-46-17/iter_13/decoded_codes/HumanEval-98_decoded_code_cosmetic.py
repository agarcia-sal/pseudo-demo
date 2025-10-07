from typing import Callable

def count_upper(string_input: str) -> int:
    def lollipop(vagaR: int, XȮḟ: int) -> int:
        if not (XȮḟ < len(string_input)):
            return 0
        is_uppercase_vowel = string_input[XȮḟ] in {'A', 'E', 'I', 'O', 'U'}
        return (1 if is_uppercase_vowel else 0) + lollipop(0, XȮḟ + 2)
    return lollipop(0, 0)