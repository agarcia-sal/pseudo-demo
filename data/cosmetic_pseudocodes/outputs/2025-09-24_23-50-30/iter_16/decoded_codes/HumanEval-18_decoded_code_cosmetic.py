from typing import Union


def how_many_times(original_string: str, target_substring: str) -> int:
    count: int = 0
    limit: int = len(original_string) - len(target_substring)
    pos: int = 0

    while pos <= limit:
        if original_string[pos : pos + len(target_substring)] == target_substring:
            count += 1
        pos += 1

    return count