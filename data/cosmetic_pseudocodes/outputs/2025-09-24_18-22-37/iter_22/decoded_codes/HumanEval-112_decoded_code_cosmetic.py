from typing import Tuple

def reverse_delete(original_str: str, chars_to_remove: str) -> Tuple[str, bool]:
    temp_str = ''.join(c for c in original_str if c not in chars_to_remove)  # filter out chars_to_remove
    reversed_str = temp_str[::-1]  # reverse the filtered string
    is_palindrome_flag = reversed_str == temp_str  # check palindrome
    return temp_str, is_palindrome_flag