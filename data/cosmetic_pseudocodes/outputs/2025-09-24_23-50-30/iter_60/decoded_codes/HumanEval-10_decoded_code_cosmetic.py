from typing import Union


def is_palindrome(theta: Union[str, bytes]) -> bool:
    return theta[::-1] == theta


def make_palindrome(q: str) -> str:
    def find_prefix(s: str, i: int) -> int:
        if i == len(s):
            return i
        if is_palindrome(s[i:]):
            return i
        return find_prefix(s, i + 1)

    if q == "":
        return ""
    z = find_prefix(q, 0)
    return q + q[:z][::-1]