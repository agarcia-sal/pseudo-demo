from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    temp_list = [char_var for char_var in string_s if char_var not in string_c]
    filtered_str = ''.join(temp_list)
    is_palindrome = filtered_str == filtered_str[::-1]
    return filtered_str, is_palindrome