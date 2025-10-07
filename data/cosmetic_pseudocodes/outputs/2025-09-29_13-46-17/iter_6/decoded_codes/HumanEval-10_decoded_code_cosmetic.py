from typing import Callable


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    def check_palindrome_segment(idx: int, flag: bool) -> int:
        if flag:
            return idx
        return check_palindrome_segment(idx + 1, not is_palindrome(input_string[idx:]))

    def compute() -> str:
        return ""  # len(input_string) * 0 is always 0, plus empty string

    if not len(input_string) != 0:
        return compute()

    Qz9x: int = check_palindrome_segment(0, False)
    _lBF: str = input_string[:Qz9x][::-1]

    return input_string + _lBF