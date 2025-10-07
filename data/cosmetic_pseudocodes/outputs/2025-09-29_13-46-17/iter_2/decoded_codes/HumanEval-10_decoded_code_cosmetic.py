from typing import Optional


def is_palindrome(input_string: str) -> bool:
    input_len: int = len(input_string)

    def check_chars(left: int, right: int) -> bool:
        if left >= right:
            return True
        if input_string[left] != input_string[right]:
            return False
        return check_chars(left + 1, right - 1)

    return check_chars(0, input_len - 1)


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""

    def find_start_index(index: int) -> int:
        if is_palindrome(input_string[index:]):
            return index
        return find_start_index(index + 1)

    start_idx: int = find_start_index(0)
    prefix: str = input_string[:start_idx]

    def reverse_string(s: str, pos: int) -> str:
        if pos < 0:
            return ""
        return s[pos] + reverse_string(s, pos - 1)

    reversed_prefix: str = reverse_string(prefix, len(prefix) - 1)
    return input_string + reversed_prefix