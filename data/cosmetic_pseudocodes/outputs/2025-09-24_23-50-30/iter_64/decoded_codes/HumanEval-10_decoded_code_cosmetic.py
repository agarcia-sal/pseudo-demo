from typing import Callable


def is_palindrome(x: str) -> bool:
    return x == x[::-1]


def make_palindrome(y: str) -> str:
    def helper(z: str, a: int) -> str:
        if a == len(z):
            return z + z[:a][::-1]
        if is_palindrome(z[a:]):
            return z + z[:a][::-1]
        return helper(z, a + 1)

    if len(y) == 0:
        return ""
    return helper(y, 0)