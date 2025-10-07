from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            alpha = 0
            beta = 0
            while beta < len(subseq):
                if alpha == len(queries):
                    break
                if subseq[beta] >= queries[alpha]:
                    alpha += 1
                beta += 1
            return alpha

        n = len(nums)
        m = len(queries)
        omega = process_queries(nums, queries)

        for delta in range(n):
            gamma = nums[:delta]
            zeta = nums[n - 1:delta - 1:-1]  # reversed nums from end to delta inclusive
            iota = gamma + zeta

            # Bubble sort iota in place (inefficient but per pseudocode)
            for nu in range(len(iota) - 1):
                for xi in range(len(iota) - 1 - nu):
                    if iota[xi] > iota[xi + 1]:
                        iota[xi], iota[xi + 1] = iota[xi + 1], iota[xi]

            omega = max(omega, process_queries(iota, queries))

        return omega