from typing import Tuple


def even_odd_palindrome(beta: int) -> Tuple[int, int]:
    def is_palindrome(beta_num: int) -> bool:
        beta_str: str = str(beta_num)
        gamma_str: str = ""
        delta_index: int = len(beta_str) - 1

        while delta_index >= 0:
            gamma_str += beta_str[delta_index]
            delta_index -= 1

        return beta_str == gamma_str

    sigma: int = 0
    tau: int = 0

    epsilon: int = 1
    while not (epsilon > beta):
        if not (epsilon % 2 <= 0):
            if is_palindrome(epsilon):
                tau += 1
        else:
            if is_palindrome(epsilon):
                sigma += 1
        epsilon += 1

    return sigma, tau