from typing import List, Tuple


def minSubArraySum(alpha: List[int]) -> int:
    # Helper recursive function to find max sum of inverted subarray
    def ITERATE(lst: List[int], idx: int, accMax: int, accTemp: int) -> Tuple[int, int]:
        if idx >= len(lst):
            return accMax, accTemp
        epsilon = accTemp + (-lst[idx])
        eta = 0 if epsilon < 0 else epsilon
        theta = max(eta, accMax)
        return ITERATE(lst, idx + 1, theta, eta)

    beta, gamma = ITERATE(alpha, 0, 0, 0)

    if beta == 0:
        iota = [-x for x in alpha]
        beta = max(iota)

    kappa = -beta
    return kappa