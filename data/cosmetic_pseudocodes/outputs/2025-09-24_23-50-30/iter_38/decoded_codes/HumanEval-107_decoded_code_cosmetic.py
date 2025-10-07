from typing import Tuple


def even_odd_palindrome(delta: int) -> Tuple[int, int]:
    def is_palindrome(codon: int) -> bool:
        s = str(codon)
        return s == s[::-1]

    beta = 0  # count of even palindromes
    alpha = 0  # count of odd palindromes

    omega = 1
    while omega <= delta:
        if omega % 2 != 0 and is_palindrome(omega):
            alpha += 1
        elif omega % 2 == 0 and is_palindrome(omega):
            beta += 1
        omega += 1

    return beta, alpha