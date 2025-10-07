from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered = ''.join(ch for ch in string_s if ch not in string_c)
    return filtered, filtered == filtered[::-1]