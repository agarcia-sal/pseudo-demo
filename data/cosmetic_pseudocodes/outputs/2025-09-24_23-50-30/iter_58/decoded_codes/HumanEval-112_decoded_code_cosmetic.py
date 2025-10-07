from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    temp_x = ""
    index_y = 1
    while index_y <= len(string_s):
        if string_s[index_y - 1] not in string_c:
            temp_x += string_s[index_y - 1]
        index_y += 1
    bool_z = temp_x == temp_x[::-1]
    return temp_x, bool_z