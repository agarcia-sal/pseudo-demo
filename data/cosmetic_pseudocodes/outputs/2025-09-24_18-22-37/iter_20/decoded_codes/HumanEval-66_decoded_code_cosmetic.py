from typing import Literal


def digitSum(string_input: str) -> int:
    alpha_temp: str = string_input
    index_counter: int = 0  # Adjusted to 0-based indexing for Python
    total_sum: int = 0
    str_length: int = len(alpha_temp)

    if alpha_temp == "":
        return 0

    while index_counter < str_length:
        current_char: str = alpha_temp[index_counter]
        ascii_val: int = ord(current_char)
        is_upper: bool = 'A' <= current_char <= 'Z'

        if is_upper:
            total_sum += ascii_val

        index_counter += 1

    return total_sum