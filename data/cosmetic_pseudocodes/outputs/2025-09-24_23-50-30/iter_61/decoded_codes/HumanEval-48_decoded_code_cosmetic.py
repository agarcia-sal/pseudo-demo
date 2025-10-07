from typing import Callable


def is_palindrome(alpha: str) -> bool:
    def helper(theta: int, omega: int) -> bool:
        while True:
            if theta >= omega:
                return True
            if alpha[theta] != alpha[omega]:
                return False
            theta += 1
            omega -= 1

    return helper(0, len(alpha) - 1)