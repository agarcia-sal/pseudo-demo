from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    list_x = [val_y for val_y in string_s if val_y not in string_c]
    str_p = ''.join(list_x)
    return str_p, str_p == str_p[::-1]