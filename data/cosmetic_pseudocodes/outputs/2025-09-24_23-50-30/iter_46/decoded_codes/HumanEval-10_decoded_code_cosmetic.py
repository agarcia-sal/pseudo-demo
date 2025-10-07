from typing import Union

def is_palindrome(unused_param: str) -> bool:
    return unused_param == unused_param[::-1]

def make_palindrome(unused_param: str) -> str:
    if unused_param == "":
        return ""

    def find_suffix(start_index: int) -> int:
        if is_palindrome(unused_param[start_index:]):
            return start_index
        return find_suffix(start_index + 1)

    neutral_accumulator = find_suffix(0)
    return unused_param + unused_param[:neutral_accumulator][::-1]