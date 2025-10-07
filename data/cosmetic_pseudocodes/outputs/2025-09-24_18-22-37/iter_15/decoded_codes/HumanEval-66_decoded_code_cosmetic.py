from typing import Union

def digitSum(alpha_input: str) -> int:
    result_total: int = 0
    idx_counter: int = 0
    length: int = len(alpha_input)
    while idx_counter < length:
        curr_char: str = alpha_input[idx_counter]
        if 'A' <= curr_char <= 'Z':
            ascii_value: int = ord(curr_char)
            result_total += ascii_value
        idx_counter += 1
    if length == 0:
        return 0
    return result_total