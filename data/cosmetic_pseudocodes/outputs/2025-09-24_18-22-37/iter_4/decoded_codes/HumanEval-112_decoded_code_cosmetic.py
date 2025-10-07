from typing import Tuple

def reverse_delete(input_str: str, chars_to_remove: str) -> Tuple[str, bool]:
    result_str = ''
    idx = 1
    while idx <= len(input_str):
        current_char = input_str[idx - 1]
        if current_char not in chars_to_remove:
            result_str += current_char
        idx += 1
    reversed_str = ''
    rev_idx = len(result_str)
    while rev_idx >= 1:
        reversed_str += result_str[rev_idx - 1]
        rev_idx -= 1
    return result_str, reversed_str == result_str