from typing import Tuple

def reverse_delete(input_string: str, chars_to_remove: str) -> Tuple[str, bool]:
    def filter_chars(str_val: str, chars_val: str, index_val: int, acc_val: str) -> str:
        if index_val == len(str_val):
            return acc_val
        if str_val[index_val] not in chars_val:
            return filter_chars(str_val, chars_val, index_val + 1, acc_val + str_val[index_val])
        return filter_chars(str_val, chars_val, index_val + 1, acc_val)

    filtered_string = filter_chars(input_string, chars_to_remove, 0, "")

    def is_palindrome(str_val: str, start_idx: int, end_idx: int) -> bool:
        if start_idx >= end_idx:
            return True
        if str_val[start_idx] != str_val[end_idx]:
            return False
        return is_palindrome(str_val, start_idx + 1, end_idx - 1)

    palindrome_flag = is_palindrome(filtered_string, 0, len(filtered_string) - 1)

    return filtered_string, palindrome_flag