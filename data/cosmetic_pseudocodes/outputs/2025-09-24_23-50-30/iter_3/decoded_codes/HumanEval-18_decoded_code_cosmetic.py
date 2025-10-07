from typing import Literal

def how_many_times(original_string: str, target_substring: str) -> int:
    count_occurrences = 0
    len_target = len(target_substring)
    max_start = len(original_string) - len_target
    position = 0
    while position <= max_start:
        if original_string[position : position + len_target] == target_substring:
            count_occurrences += 1
        position += 1
    return count_occurrences