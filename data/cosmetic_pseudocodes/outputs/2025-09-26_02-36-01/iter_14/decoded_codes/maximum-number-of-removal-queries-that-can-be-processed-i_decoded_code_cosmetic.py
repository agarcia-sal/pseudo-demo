from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            alpha = 0
            delta = 0
            while delta < len(queries):
                if alpha >= len(subseq):
                    break
                if subseq[alpha] - queries[delta] >= 0:
                    alpha += 1
                delta += 1
            return alpha

        psi = len(nums)
        gamma = process_queries(nums, queries)

        for sigma in range(psi):
            omega_prefix = nums[:sigma]
            tau_suffix = nums[psi - 1:sigma - 1:-1]  # reversed suffix from psi-1 down to sigma
            xi = omega_prefix + tau_suffix
            xi.sort()
            gamma = max(gamma, process_queries(xi, queries))

        return gamma