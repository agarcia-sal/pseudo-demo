from typing import Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def is_palindrome(zeta: T) -> bool:
    return zeta == zeta[::-1]

def make_palindrome(omega: str) -> str:
    if omega == "":
        return ""
    delta = 0
    length = len(omega)
    while not is_palindrome(omega[delta:length]):
        delta += 1
    return omega + omega[:delta][::-1]