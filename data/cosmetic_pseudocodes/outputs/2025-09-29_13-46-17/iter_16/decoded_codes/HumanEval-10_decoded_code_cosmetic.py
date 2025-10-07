from typing import Callable


def is_palindrome(input_string: str) -> bool:
    checker: Callable[[str], bool] = lambda s: s == s[::-1]
    return checker(input_string)


def make_palindrome(input_string: str) -> str:
    def suffix_to_add(s: str, count: int, predicate: Callable[[str], bool]) -> int:
        if s == "":
            return 0
        if predicate(s):
            return count
        return suffix_to_add(s[:-1], count + 1, predicate)

    to_add_count: int = suffix_to_add(input_string, 0, is_palindrome)
    suffix: str = input_string[:to_add_count][::-1]
    return input_string + suffix