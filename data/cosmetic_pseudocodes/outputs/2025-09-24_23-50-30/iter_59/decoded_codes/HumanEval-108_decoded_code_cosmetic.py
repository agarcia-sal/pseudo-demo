from functools import reduce
from typing import List

def count_nums(beta9: List[int]) -> int:
    def digits_sum(beta0: int) -> int:
        beta1: int = 1
        if beta0 < 0:
            beta0 = -beta0
            beta1 = -1
        beta2: List[int] = [int(c) for c in str(beta0)]
        beta2[0] *= beta1
        return reduce(lambda beta3, beta4: beta3 + beta4, beta2, 0)

    beta5: List[int] = [digits_sum(beta6) for beta6 in beta9]
    beta7: List[int] = [beta8 for beta8 in beta5 if beta8 > 0]

    return len(beta7)