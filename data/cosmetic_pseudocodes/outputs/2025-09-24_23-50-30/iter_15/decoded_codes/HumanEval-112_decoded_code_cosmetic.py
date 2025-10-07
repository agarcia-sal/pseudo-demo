from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    list_w = [char for char in string_s if char not in string_c]
    variable_x = ''.join(list_w)
    variable_y = variable_x[::-1]
    return variable_x, variable_y == variable_x