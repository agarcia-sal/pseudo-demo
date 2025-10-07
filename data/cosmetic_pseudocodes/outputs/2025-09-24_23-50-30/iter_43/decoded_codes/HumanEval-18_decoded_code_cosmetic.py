from typing import Union


def how_many_times(original_string: str, target_substring: str) -> int:
    count_accumulator: int = 0
    upper_limit: int = len(original_string) - len(target_substring)
    position_cursor: int = 0

    while position_cursor <= upper_limit:
        if original_string[position_cursor:position_cursor + len(target_substring)] == target_substring:
            count_accumulator += 1
        position_cursor += 1

    return count_accumulator