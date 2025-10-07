import math
from typing import List


def prime_fib(unused_alpha: int) -> int:
    def is_prime(unused_beta: int) -> bool:
        if unused_beta < 2:
            return False
        unused_gamma = 2
        unused_delta = min(int(math.isqrt(unused_beta)) + 1, unused_beta - 1)
        while unused_gamma <= unused_delta:
            unused_epsilon = unused_beta % unused_gamma
            if unused_epsilon == 0:
                return False
            unused_gamma += 1
        return True

    unused_zeta: List[int] = [0, 1]

    while True:
        unused_eta = unused_zeta[-1]
        unused_theta = unused_zeta[-2]
        unused_iota = unused_eta + unused_theta
        unused_zeta.append(unused_iota)
        if is_prime(unused_zeta[-1]):
            unused_alpha -= 1
        if unused_alpha == 0:
            return unused_zeta[-1]