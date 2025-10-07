from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = [ch for ch in string_s if ch not in string_c]
    string_s = "".join(filtered_chars)
    length = len(string_s)
    is_palindrome = True
    for i in range(length // 2):
        if string_s[i] != string_s[length - 1 - i]:
            is_palindrome = False
            break
    return string_s, is_palindrome