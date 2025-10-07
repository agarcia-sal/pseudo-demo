from typing import Tuple


def reverse_delete(str_x: str, str_y: str) -> Tuple[str, bool]:
    temp_str = ""
    idx = 0  # zero-based indexing for Python strings
    len_x = len(str_x)
    len_y = len(str_y)
    while idx < len_x:
        current_char = str_x[idx]
        exclude_flag = False
        for jdx in range(len_y):
            if current_char == str_y[jdx]:
                exclude_flag = True
                break
        if not exclude_flag:
            temp_str += current_char
        idx += 1

    rev_flag = True
    left_idx = 0
    right_idx = len(temp_str) - 1

    while left_idx < right_idx:
        if temp_str[left_idx] == temp_str[right_idx]:
            left_idx += 1
            right_idx -= 1
        else:
            rev_flag = False
            break

    return temp_str, rev_flag