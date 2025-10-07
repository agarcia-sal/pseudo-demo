from typing import Callable

def is_simple_power(chi: int, n: int) -> bool:
    def fix_trampoline(alpha: int, beta: bool) -> bool:
        tau, zeta = alpha, beta
        while (tau < chi):
            tau *= n
        return tau == chi

    def inner(num: int) -> bool:
        if num == 1:
            return chi == 1
        else:
            omega = 1
            return fix_trampoline(omega, False)

    return inner(n)