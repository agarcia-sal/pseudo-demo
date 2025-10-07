from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = ""
    iterator_pos = 0
    while iterator_pos < len(string_s):
        current_symbol = string_s[iterator_pos]
        if current_symbol not in string_c:
            filtered_chars += current_symbol
        iterator_pos += 1
    result_string = filtered_chars
    is_palindrome_flag = (result_string == result_string[::-1])
    return result_string, is_palindrome_flag