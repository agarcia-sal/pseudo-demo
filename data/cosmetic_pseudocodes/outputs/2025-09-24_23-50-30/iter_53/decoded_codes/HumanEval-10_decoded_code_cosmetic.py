from typing import Callable


def is_palindrome(x: str) -> bool:
    return x == x[::-1]


def make_palindrome(y: str) -> str:
    if not y:
        return ""
    else:
        def loop(b: int) -> int:
            if is_palindrome(y[b:]):
                return b
            else:
                return loop(b + 1)
        c: int = loop(0)
        return y + y[:c][::-1]