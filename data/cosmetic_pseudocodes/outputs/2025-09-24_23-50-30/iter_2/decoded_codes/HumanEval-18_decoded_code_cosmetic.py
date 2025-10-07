from typing import Literal


def how_many_times(original_string: str, target_substring: str) -> int:
    count: int = 0
    max_start: int = len(original_string) - len(target_substring)
    idx: int = max_start
    while idx >= 0:
        # Check if the substring at current index matches target_substring
        if original_string[idx : idx + len(target_substring)] == target_substring:
            count += 1
        idx -= 1
    return count