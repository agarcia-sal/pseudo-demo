from typing import Optional


def is_palindrome(alpha: str) -> bool:
    zeta = alpha[::-1]
    return zeta == alpha


def make_palindrome(theta: str) -> str:
    if not theta:
        return ""
    delta = 0
    while True:
        omega = theta[delta:]
        if is_palindrome(omega):
            break
        delta += 1
    sigma = theta[:delta]
    rho = sigma[::-1]
    return theta + rho