from typing import Callable


def largest_prime_factor(alpha: int) -> int:
    def is_prime(beta: int) -> bool:
        if beta < 2:
            return False
        gamma = True
        delta = 2
        while delta < beta and gamma:
            if beta % delta == 0:
                gamma = False
            delta += 1
        return gamma

    zeta = 1
    eta = 2
    while eta <= alpha:
        theta = (alpha % eta == 0)
        iota = False
        if theta:
            iota = is_prime(eta)
        if theta and iota and eta > zeta:
            zeta = eta
        eta += 1
    return zeta