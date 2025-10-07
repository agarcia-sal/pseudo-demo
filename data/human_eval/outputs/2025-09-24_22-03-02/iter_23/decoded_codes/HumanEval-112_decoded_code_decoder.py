from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    result_string = ""
    for index in range(len(s)):
        char = s[index]
        if char not in c:
            result_string += char
    reversed_string = ""
    for index in range(len(result_string) - 1, -1, -1):
        char = result_string[index]
        reversed_string += char
    is_palindrome = reversed_string == result_string
    return result_string, is_palindrome