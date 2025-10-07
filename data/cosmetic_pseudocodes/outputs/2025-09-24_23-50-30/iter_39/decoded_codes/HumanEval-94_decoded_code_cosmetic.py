from typing import List

def skjkasdkd(array_alpha: List[int]) -> int:
    def isPrime(beta: int) -> bool:
        if beta < 2:
            return False
        gamma = 2
        while gamma * gamma <= beta:
            if beta % gamma == 0:
                return False
            gamma += 1
        return True

    delta = 0
    epsilon = 0

    while epsilon < len(array_alpha):
        if array_alpha[epsilon] > delta and isPrime(array_alpha[epsilon]):
            delta = array_alpha[epsilon]
            # Once updated, skip remaining cases: same effect as break in switch
        epsilon += 1

    zeta = 0
    for character_sigma in str(delta):
        theta = int(character_sigma)
        zeta += theta

    return zeta