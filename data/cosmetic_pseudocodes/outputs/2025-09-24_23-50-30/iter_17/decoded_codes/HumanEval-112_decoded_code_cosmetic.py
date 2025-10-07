from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    list_x = [ch for ch in string_s if ch not in string_c]
    string_y = ''.join(list_x)
    return (string_y, string_y == string_y[::-1])