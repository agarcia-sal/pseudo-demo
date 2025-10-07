from typing import Callable

def vowels_count(string_input: str) -> int:
    V: str = "aeiouAEIOU"

    def count_chars(idx: int) -> int:
        if idx >= len(string_input):
            return 0
        current_char: str = string_input[idx]
        increment: int = int(current_char in V)
        return increment + count_chars(idx + 1)

    total: int = count_chars(0)
    last_idx: int = len(string_input) - 1
    if last_idx >= 0:
        tail_char: str = string_input[last_idx]
        if tail_char in ('y', 'Y'):
            total += 1
    return total