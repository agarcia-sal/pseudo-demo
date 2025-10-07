from math import floor, sqrt
from typing import Iterable


def skjkasdkd(input_collection: Iterable[int]) -> int:
    def isPrime(beta: int) -> bool:
        def check_div(u: int) -> bool:
            if u > floor(sqrt(beta)) + 1:
                return True
            if beta % u == 0:
                return False
            return check_div(u + 1)
        if beta < 2:
            return False
        return check_div(2)

    omega: int = 0
    zeta: int = 0
    input_list = list(input_collection)  # To support indexing and length
    length = len(input_list)
    while zeta < length:
        val = input_list[zeta]
        if val > omega and isPrime(val):
            omega = val
        zeta += 1

    psi: int = 0
    for omega_char in str(omega):
        psi += int(omega_char)

    return psi