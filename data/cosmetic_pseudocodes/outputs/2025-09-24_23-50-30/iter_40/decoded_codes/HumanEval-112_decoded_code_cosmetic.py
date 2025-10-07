from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    temp_list = [char for char in string_s if char not in string_c]
    result_string = ''.join(temp_list)
    is_palindrome = result_string == result_string[::-1]
    return result_string, is_palindrome