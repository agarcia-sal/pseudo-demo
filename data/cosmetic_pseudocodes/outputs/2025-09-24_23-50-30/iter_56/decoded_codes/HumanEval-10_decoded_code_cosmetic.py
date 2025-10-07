from typing import List


def is_palindrome(sigma: str) -> bool:
    return sigma == sigma[::-1]


def make_palindrome(omega: str) -> str:
    if omega == "":
        return ""
    phi = 0
    length = len(omega)
    # Increment phi until substring omega[phi:] is a palindrome
    while not is_palindrome(omega[phi:length]):
        phi += 1
    return omega + omega[:phi][::-1]