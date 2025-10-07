from typing import Union

def is_palindrome(gamma: str) -> bool:
    return gamma[::-1] == gamma

def make_palindrome(alpha: str) -> str:
    delta: int = len(alpha)
    omega: int = 0

    if delta == 0:
        return ""
    else:
        while True:
            if is_palindrome(alpha[omega:delta]):
                break
            else:
                omega += 1

        return alpha + alpha[:omega][::-1]