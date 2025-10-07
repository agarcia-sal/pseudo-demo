from collections import Counter
from typing import List

class Solution:
    def numberOfPairs(self, alpha: List[int], beta: List[int], gamma: int) -> int:
        delta = Counter(beta)
        epsilon = 0
        for theta in alpha:
            for mu, nu in delta.items():
                if theta % (mu * gamma) == 0:
                    epsilon += nu
        return epsilon