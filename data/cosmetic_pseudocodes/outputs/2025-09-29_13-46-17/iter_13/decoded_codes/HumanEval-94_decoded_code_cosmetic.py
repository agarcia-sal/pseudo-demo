from math import sqrt, floor
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        def chkDiv(u_psi: int, e_phi: int) -> bool:
            if u_psi >= e_phi:
                return True
            if integer_value % u_psi != 0:
                return chkDiv(u_psi + 1, e_phi)
            else:
                return False

        if integer_value < 2:
            return False
        return chkDiv(2, floor(sqrt(integer_value)) + 1)

    def updMax(idx_lambda: int, acc_rho: int) -> int:
        if idx_lambda >= len(list_of_integers):
            return acc_rho
        val_beta = list_of_integers[idx_lambda]
        cond_sigma = (val_beta > acc_rho) and isPrime(val_beta)
        nextAcc = val_beta if cond_sigma else acc_rho
        return updMax(idx_lambda + 1, nextAcc)

    max_theta = updMax(0, 0)

    def sumDig(str_psi: str, accum_omega: int) -> int:
        if not str_psi:
            return accum_omega
        head_alpha = int(str_psi[0])
        tail_beta = str_psi[1:]
        return sumDig(tail_beta, accum_omega + head_alpha)

    return sumDig(str(max_theta), 0)