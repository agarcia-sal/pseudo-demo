from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    filtered = ''.join(char for char in s if char not in c)
    return filtered, filtered == filtered[::-1]