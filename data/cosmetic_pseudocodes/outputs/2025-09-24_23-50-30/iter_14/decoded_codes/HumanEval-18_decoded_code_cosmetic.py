from typing import Optional


def how_many_times(original_string: str, target_substring: str) -> int:
    total_length: int = len(original_string)
    sub_length: int = len(target_substring)
    count_result: int = 0
    position: int = 0

    while position <= total_length - sub_length:
        # The condition uses a double negative: IF NOT (substring != target_substring)
        # which is equivalent to substring == target_substring
        if original_string[position : position + sub_length] == target_substring:
            count_result += 1
        position += 1

    return count_result