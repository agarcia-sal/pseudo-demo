from math import sqrt, floor
from typing import List


def skjkasdkd(alpha_list: List[int]) -> int:
    def isPrime(beta_num: int) -> bool:
        def testDiv(gamma: int, delta: int) -> bool:
            if gamma > delta:
                return True
            if beta_num % gamma == 0:
                return False
            return testDiv(gamma + 1, delta)

        if beta_num < 2:
            return False
        return testDiv(2, floor(sqrt(beta_num)) + 1)

    omega: int = 0
    psi: int = 0
    lambda_limit: int = len(alpha_list)

    while psi < lambda_limit:
        current_val = alpha_list[psi]
        if current_val > omega and isPrime(current_val):
            omega = current_val
        psi += 1

    def addDigits(str_num: str, idx: int, acc: int) -> int:
        if idx == len(str_num):
            return acc
        return addDigits(str_num, idx + 1, acc + int(str_num[idx]))

    rho: int = addDigits(str(omega), 0, 0)

    return rho