from typing import Optional


def is_palindrome(s: str) -> bool:
    temp_rev: str = s[::-1]
    equality_check: bool = (s == temp_rev)
    return equality_check


def make_palindrome(t: str) -> str:
    if t == "":
        return ""

    idx: int = 0
    test_substr: str = t[idx:]

    while not is_palindrome(test_substr):
        idx += 1
        test_substr = t[idx:]

    front_part: str = t[:idx]
    reverse_front: str = front_part[::-1]
    result_str: str = t + reverse_front
    return result_str