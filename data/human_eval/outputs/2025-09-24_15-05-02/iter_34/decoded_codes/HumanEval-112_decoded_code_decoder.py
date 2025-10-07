from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    string_s = ''.join(ch for ch in string_s if ch not in string_c)
    return string_s, string_s == string_s[::-1]