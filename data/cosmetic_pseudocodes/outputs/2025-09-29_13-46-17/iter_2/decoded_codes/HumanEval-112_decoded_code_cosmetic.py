from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def filter_chars(s: str, c: str, idx: int, result: str) -> str:
        if idx >= len(s):
            return result
        if s[idx] not in c:
            result += s[idx]
        return filter_chars(s, c, idx + 1, result)

    filtered = filter_chars(string_s, string_c, 0, "")
    is_palindrome = filtered == filtered[::-1]
    return filtered, is_palindrome