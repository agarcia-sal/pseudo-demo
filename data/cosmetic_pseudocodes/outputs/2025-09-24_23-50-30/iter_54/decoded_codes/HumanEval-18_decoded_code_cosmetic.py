from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    def inner_count(current_pos: int, acc: int) -> int:
        if current_pos > len(original_string) - len(target_substring):
            return acc
        return inner_count(
            current_pos + 1,
            acc + (1 if original_string[current_pos : current_pos + len(target_substring)] == target_substring else 0)
        )
    return inner_count(0, 0)