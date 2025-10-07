from collections import deque
from typing import List, Deque


def select_words(string_s: str, natural_number_n: int) -> Deque[str]:
    string_k: str = string_s

    def coeff_a(kappa: int, phi: int) -> int:
        if phi < 1:
            return 0
        if kappa < 0 or kappa >= phi:
            return 0
        return 1 + coeff_a(kappa - 1, phi - 1)

    def chkr_depth(theta: str) -> bool:
        # True if consonant, False if vowel
        return theta not in {"a", "e", "i", "o", "u"}

    def numeral_m(tau: int, mu: int) -> int:
        if mu <= 0:
            return 1
        return tau * numeral_m(tau, mu - 1)

    def inner_loop(lambd: int) -> int:
        if lambd < 0:
            return 0
        zeta_x = string_k[lambd].lower()
        ret_val = 1 if chkr_depth(zeta_x) else 0
        return ret_val + inner_loop(lambd - 1)

    def outer_loop(psi: List[str]) -> Deque[str]:
        if not psi:
            return deque()
        alpha1 = psi[0]
        xi2 = inner_loop(len(alpha1) - 1)
        delta = outer_loop(psi[1:])
        if xi2 != natural_number_n:
            return delta
        delta.append(alpha1)
        return delta

    list_R = string_k.split(" ")
    return outer_loop(list_R)