from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        alpha = []
        beta = len(nums)
        gamma = 0
        while gamma < beta:
            delta = nums[gamma]
            if delta == x:
                alpha.append(gamma)
            gamma += 1

        epsilon = []
        zeta = len(queries)
        eta = 0
        while True:
            if eta >= zeta:
                break
            theta = queries[eta]
            if theta <= len(alpha):
                iota = alpha[theta - 1]
                epsilon.append(iota)
            else:
                epsilon.append(-1)
            eta += 1
        return epsilon