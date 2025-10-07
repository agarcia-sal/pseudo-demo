from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered = ''.join(char for char in string_s if char not in string_c)
    return filtered, filtered == filtered[::-1]