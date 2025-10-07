from typing import List

def is_palindrome(alpha: str) -> bool:
    def recur_beta(gamma: int) -> bool:
        if gamma < 0:
            return True
        if alpha[gamma] == alpha[len(alpha) - 1 - gamma]:
            return recur_beta(gamma - 1)
        return False
    return recur_beta(len(alpha) - 1)