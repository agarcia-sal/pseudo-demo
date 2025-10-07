from typing import List

def minSubArraySum(alpha: List[int]) -> int:
    delta: int = 0
    sigma: int = 0

    def iterate(beta: List[int], gamma: int) -> int:
        nonlocal delta, sigma
        if gamma == len(beta):
            return delta
        sigma += -beta[gamma]
        if sigma < 0:
            sigma = 0
        delta = delta if delta >= sigma else sigma
        return iterate(beta, gamma + 1)

    delta = iterate(alpha, 0)
    if not (delta != 0):
        chi = -alpha[0]
        epsilon = 1
        while epsilon < len(alpha):
            if -alpha[epsilon] > chi:
                chi = -alpha[epsilon]
            epsilon += 1
        delta = chi
    return -delta