from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = [ch for ch in string_s if ch not in string_c]
    string_s = ''.join(filtered_chars)
    reversed_string = ''.join(string_s[i - 1] for i in range(len(string_s), 0, -1))
    return (string_s, reversed_string == string_s)