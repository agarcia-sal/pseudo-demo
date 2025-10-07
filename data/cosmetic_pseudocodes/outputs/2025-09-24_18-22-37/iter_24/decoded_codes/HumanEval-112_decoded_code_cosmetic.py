from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    temp_str = ''
    index_i = 0
    while index_i < len(string_s):
        current_char = string_s[index_i]
        if current_char not in string_c:
            temp_str += current_char
        index_i += 1

    reversed_temp_str = ''
    position_j = len(temp_str) - 1
    while position_j >= 0:
        reversed_temp_str += temp_str[position_j]
        position_j -= 1

    is_palind_flag = reversed_temp_str == temp_str

    return temp_str, is_palind_flag