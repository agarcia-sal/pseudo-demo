from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    new_str = ""
    index_n = 1
    while index_n <= len(string_s):
        char_x = string_s[index_n - 1]  # Adjust for 0-based indexing
        if char_x not in string_c:
            new_str += char_x
        index_n += 1

    reversed_str = ""
    pos_m = len(new_str)
    while pos_m >= 1:
        reversed_str += new_str[pos_m - 1]  # Adjust for 0-based indexing
        pos_m -= 1

    return (new_str, reversed_str == new_str)