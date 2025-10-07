from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def helper(s: str, length: int) -> Tuple[str, bool]:
        if length == 0:
            return "", True
        prev_str, prev_bool = helper(s, length - 1)
        current_char = s[length - 1]
        if current_char not in string_c:
            # Check if the current char matches the corresponding char from the end of prev_str
            is_palindrome = prev_bool and (current_char == prev_str[len(prev_str) - length])
            return current_char + prev_str, is_palindrome
        else:
            return prev_str, prev_bool

    n = len(string_s)
    filtered_str, is_palindrome = helper(string_s, n)
    return filtered_str, is_palindrome