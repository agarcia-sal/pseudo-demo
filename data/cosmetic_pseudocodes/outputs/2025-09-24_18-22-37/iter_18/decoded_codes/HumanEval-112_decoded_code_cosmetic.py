from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    result_str = ""
    index_a = 0
    while index_a < len(string_s):
        char_temp = string_s[index_a]
        found_flag = False
        index_b = 0
        while index_b < len(string_c) and not found_flag:
            if string_c[index_b] == char_temp:
                found_flag = True
            index_b += 1
        if not found_flag:
            result_str += char_temp
        index_a += 1

    reversed_str = ""
    idx_rev = len(result_str) - 1
    while idx_rev >= 0:
        reversed_str += result_str[idx_rev]
        idx_rev -= 1

    is_palind = reversed_str == result_str

    return result_str, is_palind