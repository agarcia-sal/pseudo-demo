from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = []
    index_p = 0
    while index_p < len(string_s):
        curr_char = string_s[index_p]
        if curr_char not in string_c:
            filtered_chars.append(curr_char)
        index_p += 1
    new_string = ''.join(filtered_chars)

    comparison_result = True
    left_i = 0
    right_j = len(new_string) - 1
    while left_i < right_j and comparison_result:
        if new_string[left_i] != new_string[right_j]:
            comparison_result = False
        else:
            left_i += 1
            right_j -= 1

    return new_string, comparison_result