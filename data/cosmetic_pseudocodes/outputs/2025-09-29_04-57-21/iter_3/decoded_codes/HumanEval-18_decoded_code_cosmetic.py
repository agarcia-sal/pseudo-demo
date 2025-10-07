from typing import Union


def how_many_times(original_string: str, target_substring: str) -> int:
    total_occurrences: int = 0
    max_start_index: int = len(original_string) - len(target_substring)
    current_position: int = 0

    while current_position <= max_start_index:
        segment: str = original_string[current_position : current_position + len(target_substring)]
        if segment == target_substring:
            total_occurrences += 1
        current_position += 1

    return total_occurrences