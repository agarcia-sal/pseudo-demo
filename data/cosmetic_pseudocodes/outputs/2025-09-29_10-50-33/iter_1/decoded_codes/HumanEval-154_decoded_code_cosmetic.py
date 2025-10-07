from typing import Union

def cycpattern_check(string_a: str, string_b: str) -> bool:
    length_b: int = len(string_b)
    doubled_pattern: str = string_b + string_b
    max_start: int = len(string_a) - length_b

    if length_b == 0 or max_start < 0:
        # No valid substrings if string_b is empty or longer than string_a
        return False

    for start_pos in range(max_start + 1):
        candidate_substring: str = string_a[start_pos:start_pos + length_b]
        for offset in range(length_b + 1):
            pattern_substring: str = doubled_pattern[offset:offset + length_b]
            if candidate_substring == pattern_substring:
                return True

    return False