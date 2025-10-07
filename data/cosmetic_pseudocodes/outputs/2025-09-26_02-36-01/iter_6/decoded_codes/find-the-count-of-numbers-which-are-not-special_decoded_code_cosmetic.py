import math

class Solution:
    def nonSpecialCount(self, alpha: int, beta: int) -> int:
        def is_prime(gamma: int) -> bool:
            if gamma <= 1:
                return False
            if gamma <= 3:
                return True
            if gamma % 2 == 0 or gamma % 3 == 0:
                return False
            delta = 5
            while delta * delta <= gamma:
                if gamma % delta == 0 or gamma % (delta + 2) == 0:
                    return False
                delta += 6
            return True

        eta = math.ceil(math.sqrt(alpha))
        theta = math.floor(math.sqrt(beta))

        iota = 0
        kappa = eta
        while kappa <= theta:
            if is_prime(kappa):
                iota += 1
            kappa += 1

        lambda_ = (beta - alpha + 1)
        return lambda_ - iota