from typing import Callable


def count_upper(string_input: str) -> int:
    def helper(pos: int, total: int) -> int:
        if pos >= len(string_input):
            return total
        current_char = string_input[pos]
        is_vowel = current_char in {'A', 'E', 'I', 'O', 'U'}
        return helper(pos + 2, total + int(is_vowel))

    return helper(0, 0)