from typing import Tuple

def reverse_delete(string_p: str, string_q: str) -> Tuple[str, bool]:
    string_r = ''.join(symbol for symbol in string_p if symbol not in string_q)
    boolean_x = string_r == string_r[::-1]
    return string_r, boolean_x