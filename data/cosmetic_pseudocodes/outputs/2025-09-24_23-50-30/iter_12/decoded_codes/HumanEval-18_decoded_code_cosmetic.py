from typing import AnyStr


def how_many_times(original_string: AnyStr, target_substring: AnyStr) -> int:
    count_occurrences: int = 0
    limit: int = len(original_string) - len(target_substring)
    index: int = 0

    while index <= limit:
        if original_string[index : index + len(target_substring)] == target_substring:
            count_occurrences += 1
        index += 1

    return count_occurrences