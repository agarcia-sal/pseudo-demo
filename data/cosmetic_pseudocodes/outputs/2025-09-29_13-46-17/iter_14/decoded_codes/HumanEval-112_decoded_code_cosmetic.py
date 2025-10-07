from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def filtered_string(s: str, c: str) -> str:
        # Build a new string with chars in s but not in c
        return ''.join(ch for ch in s if ch not in c)

    filtered = filtered_string(string_s, string_c)

    def is_palindrome(s: str) -> bool:
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and is_palindrome(s[1:-1])

    return filtered, is_palindrome(filtered)