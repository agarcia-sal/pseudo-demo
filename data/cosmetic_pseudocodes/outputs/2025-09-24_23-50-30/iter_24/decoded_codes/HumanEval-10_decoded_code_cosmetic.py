from typing import Callable


def is_palindrome(alfa: str) -> bool:
    return alfa == alfa[::-1]


def make_palindrome(beta: str) -> str:
    def seek(index: int) -> int:
        if index == len(beta):
            return index
        if not is_palindrome(beta[index:]):
            return seek(index + 1)
        return index

    if len(beta) == 0:
        return ""
    gamma = seek(0)
    return beta + beta[:gamma][::-1]