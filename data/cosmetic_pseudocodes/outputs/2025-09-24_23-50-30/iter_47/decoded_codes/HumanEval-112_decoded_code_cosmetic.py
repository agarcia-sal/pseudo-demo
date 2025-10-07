from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    # Collect characters from string_s not in string_c
    list_x = [char for char in string_s if char not in string_c]
    string_y = ''.join(list_x)
    boolean_z = string_y == string_y[::-1]
    return string_y, boolean_z