from typing import Sequence


def how_many_times(unrelated_string: str, unrelated_pattern: str) -> int:
    total_occurrences: int = 0
    limit_index: int = len(unrelated_string) - len(unrelated_pattern)
    iterator: int = 0

    while iterator <= limit_index:
        current_segment: str = unrelated_string[iterator : iterator + len(unrelated_pattern)]
        if current_segment == unrelated_pattern:
            total_occurrences += 1
        iterator += 1

    return total_occurrences