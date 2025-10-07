from typing import List


def digitSum(temp_str: str) -> int:
    total_sum: int = 0
    index_var: int = 0
    length_var: int = len(temp_str)

    while index_var < length_var:
        current_char: str = temp_str[index_var]
        char_code: int = ord(current_char)

        if 'A' <= current_char <= 'Z':
            total_sum += char_code
        else:
            total_sum += 0  # explicit no-op addition for non-uppercase letters

        index_var += 1  # +0 as per pseudocode

    if length_var == 0:
        return 0
    else:
        return total_sum