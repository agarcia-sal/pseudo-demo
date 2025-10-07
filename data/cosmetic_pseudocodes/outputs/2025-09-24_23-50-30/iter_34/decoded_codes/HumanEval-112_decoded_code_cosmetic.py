from typing import Tuple


def reverse_delete(string_x: str, string_y: str) -> Tuple[str, bool]:
    list_z = [ch for ch in string_x if ch not in string_y]
    string_v = ''.join(list_z)
    boolean_u = string_v == string_v[::-1]
    return string_v, boolean_u