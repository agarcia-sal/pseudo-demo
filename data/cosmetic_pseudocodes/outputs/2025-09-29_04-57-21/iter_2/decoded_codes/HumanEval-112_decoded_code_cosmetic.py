from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars: list[str] = [ch for ch in string_s if ch not in string_c]
    new_str: str = ''.join(filtered_chars)
    reversed_str: str = ''.join(new_str[i] for i in range(len(new_str) - 1, -1, -1))
    return new_str, reversed_str == new_str