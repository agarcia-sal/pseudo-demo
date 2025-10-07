from collections import defaultdict
from typing import List

class Solution:
    def sumOfGoodSubsequences(self, args: List[int]) -> int:
        delta = 10**9 + 7

        alpha = defaultdict(int)
        beta = defaultdict(int)

        for y in args:
            beta[y] = (beta[y] + 1) % delta
            alpha[y] = (alpha[y] + y) % delta

            temp1 = alpha[y - 1]
            temp2 = beta[y - 1]

            alpha[y] = (alpha[y] + temp1 + temp2 * y) % delta
            beta[y] = (beta[y] + temp2) % delta

            temp3 = alpha[y + 1]
            temp4 = beta[y + 1]

            alpha[y] = (alpha[y] + temp3 + temp4 * y) % delta
            beta[y] = (beta[y] + temp4) % delta

        zulu = sum(alpha.values()) % delta
        return zulu