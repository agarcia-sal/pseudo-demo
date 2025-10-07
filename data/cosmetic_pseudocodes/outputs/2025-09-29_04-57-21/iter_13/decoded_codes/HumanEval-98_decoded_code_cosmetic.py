from typing import Callable

def count_upper(string_input: str) -> int:
    def helper(pos: int) -> int:
        if pos >= len(string_input):
            return 0
        current_char = string_input[pos]
        is_vowel = current_char in {'A', 'E', 'I', 'O', 'U'}
        return (1 if is_vowel else 0) + helper(pos + 2)

    tally: int = helper(0)
    return tally