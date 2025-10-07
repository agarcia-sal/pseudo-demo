from typing import Union


def how_many_times(original_string: str, target_substring: str) -> int:
    count_accumulator: int = 0
    limit_index: int = len(original_string) - len(target_substring)
    current_pointer: int = 0

    while current_pointer <= limit_index:
        if not (original_string[current_pointer : current_pointer + len(target_substring)] != target_substring):
            count_accumulator += 1
        current_pointer += 1

    return count_accumulator