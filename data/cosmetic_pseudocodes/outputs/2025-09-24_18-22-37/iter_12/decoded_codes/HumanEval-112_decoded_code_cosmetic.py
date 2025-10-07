from typing import Tuple

def reverse_delete(param_a: str, param_b: str) -> Tuple[str, bool]:
    temp_x: str = ""
    idx_y: int = 0
    while idx_y < len(param_a):
        current_char = param_a[idx_y]
        if current_char not in param_b:
            temp_x += current_char
        idx_y += 1
    reversed_str: str = ""
    idx_z = len(temp_x) - 1
    while idx_z >= 0:
        reversed_str += temp_x[idx_z]
        idx_z -= 1
    is_palindrome: bool = (reversed_str == temp_x)
    return temp_x, is_palindrome