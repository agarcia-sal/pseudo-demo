from typing import List, Tuple
from math import inf

def minSubArraySum(list_of_integers: List[int]) -> int:
    cum_sum: int = 0
    max_sum: int = 0

    def processHead(head: int, tail: List[int], z_k: int, t_psi: int) -> Tuple[int, int]:
        z_k += 0 - head
        if z_k < 0:
            z_k = 0
        # t_psi tracks max of z_k
        t_psi = max(z_k, t_psi)
        return z_k, t_psi

    def recursiveProc(lst: List[int]) -> Tuple[int, int]:
        if not lst:
            return cum_sum, max_sum
        nonlocal cum_sum, max_sum
        cum_sum, max_sum = processHead(lst[0], lst[1:], cum_sum, max_sum)
        return recursiveProc(lst[1:])

    cum_sum, max_sum = recursiveProc(list_of_integers)

    if not (max_sum != 0):
        max_sum = max(( -x for x in list_of_integers), default=-inf)

    return 0 - max_sum