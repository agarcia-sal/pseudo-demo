from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars: list[str] = []
    index: int = 0
    while index < len(string_s):
        if string_s[index] not in string_c:
            filtered_chars.append(string_s[index])
        index += 1
    result_string: str = "".join(filtered_chars)

    def is_palindrome(s: str, start: int, end: int) -> bool:
        if start >= end:
            return True
        if s[start] != s[end]:
            return False
        return is_palindrome(s, start + 1, end - 1)

    return result_string, is_palindrome(result_string, 0, len(result_string) - 1)