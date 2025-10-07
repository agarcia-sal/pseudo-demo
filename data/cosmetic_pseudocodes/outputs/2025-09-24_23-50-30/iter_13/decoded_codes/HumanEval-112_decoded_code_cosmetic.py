from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    result_chars: list[str] = []
    index: int = 0
    while index < len(string_s):
        current_char: str = string_s[index]
        if current_char not in string_c:
            result_chars.append(current_char)
        index += 1
    filtered_string: str = "".join(result_chars)
    is_palindrome: bool = filtered_string == filtered_string[::-1]
    return filtered_string, is_palindrome