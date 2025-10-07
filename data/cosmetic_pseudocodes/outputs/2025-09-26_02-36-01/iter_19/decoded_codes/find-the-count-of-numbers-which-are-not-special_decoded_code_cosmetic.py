import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(tau: int) -> bool:
            if tau <= 1:
                return False
            if tau <= 3:
                return True
            if tau % 2 == 0 or tau % 3 == 0:
                return False
            omega = 5
            while omega * omega <= tau:
                if tau % omega == 0 or tau % (omega + 2) == 0:
                    return False
                omega += 6
            return True

        delta = math.ceil(math.sqrt(l))
        gamma = math.floor(math.sqrt(r))
        zeta = 0

        kappa = delta
        while kappa <= gamma:
            if is_prime(kappa):
                zeta += 1
            kappa += 1

        eta = (r - l) + 1
        return eta - zeta