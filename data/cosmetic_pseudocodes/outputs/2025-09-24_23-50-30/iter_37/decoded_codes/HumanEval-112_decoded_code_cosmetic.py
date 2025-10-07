from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    temp_u = [char_x for char_x in string_s if char_x not in string_c]
    temp_u_str = ''.join(temp_u)
    bool_v = temp_u_str == temp_u_str[::-1]
    return temp_u_str, bool_v