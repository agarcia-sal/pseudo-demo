from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_seq = [item for item in string_s if item not in string_c]
    result_str = ''.join(filtered_seq)
    is_palindrome_flag = (result_str == result_str[::-1])
    return result_str, is_palindrome_flag