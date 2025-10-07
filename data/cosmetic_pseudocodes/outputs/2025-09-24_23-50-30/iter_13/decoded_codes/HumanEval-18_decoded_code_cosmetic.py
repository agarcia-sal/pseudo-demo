from typing import Literal


def how_many_times(original_string: str, target_substring: str) -> int:
    total_occurrences = 0
    max_start_index = len(original_string) - len(target_substring)
    current_pos = 0
    while current_pos <= max_start_index:
        snippet = original_string[current_pos : current_pos + len(target_substring)]
        if snippet == target_substring:
            total_occurrences += 1
        current_pos += 1
    return total_occurrences