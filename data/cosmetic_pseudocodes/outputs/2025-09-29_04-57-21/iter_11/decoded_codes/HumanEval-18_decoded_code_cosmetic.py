from typing import Any

def how_many_times(original_string: str, target_substring: str) -> int:
    match_counter: int = 0
    start_position: int = 0
    max_start: int = len(original_string) - len(target_substring)

    while start_position <= max_start:
        if original_string[start_position : start_position + len(target_substring)] == target_substring:
            match_counter += 1
        start_position += 1

    return match_counter