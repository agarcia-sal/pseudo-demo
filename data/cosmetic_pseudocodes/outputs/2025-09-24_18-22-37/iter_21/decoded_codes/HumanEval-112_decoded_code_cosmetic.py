from typing import Tuple

def reverse_delete(str_x: str, str_y: str) -> Tuple[str, bool]:
    # Remove all characters from str_x that appear in str_y
    idx: int = 0
    result_chars = []
    while idx < len(str_x):
        curr_char = str_x[idx]
        if curr_char not in str_y:
            result_chars.append(curr_char)
        idx += 1
    str_x = ''.join(result_chars)
    return str_x, str_x == str_x[::-1]