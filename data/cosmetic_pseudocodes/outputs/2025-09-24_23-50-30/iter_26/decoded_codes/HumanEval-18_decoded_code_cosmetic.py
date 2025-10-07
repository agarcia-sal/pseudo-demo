from typing import Callable

def how_many_times(input_phrase: str, pattern: str) -> int:
    pattern_len = len(pattern)
    input_len = len(input_phrase)

    def count_helper(current_pos: int, total_count: int) -> int:
        if current_pos > input_len - pattern_len:
            return total_count
        return count_helper(
            current_pos + 1,
            total_count + (1 if input_phrase[current_pos:current_pos + pattern_len] == pattern else 0)
        )

    return count_helper(0, 0)