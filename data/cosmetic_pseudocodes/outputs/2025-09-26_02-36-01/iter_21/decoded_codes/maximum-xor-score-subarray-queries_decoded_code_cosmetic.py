from typing import List, Tuple

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        alpha = len(nums)
        beta = [[0] * alpha for _ in range(alpha)]
        gamma = [[0] * alpha for _ in range(alpha)]

        # Fill beta and gamma matrices
        m = alpha - 1
        while m >= 0:
            beta[m][m] = nums[m]
            gamma[m][m] = nums[m]
            n = m + 1
            while n < alpha:
                beta[m][n] = beta[m][n - 1] ^ beta[m + 1][n]
                candidate1 = beta[m][n]
                candidate2 = gamma[m][n - 1]
                candidate3 = gamma[m + 1][n]
                maxVal = candidate1
                if candidate2 > maxVal:
                    maxVal = candidate2
                if candidate3 > maxVal:
                    maxVal = candidate3
                gamma[m][n] = maxVal
                n += 1
            m -= 1

        def retrieveMaxVal(pair: Tuple[int, int]) -> int:
            firstIndex, secondIndex = pair
            return gamma[firstIndex][secondIndex]

        resultList = []
        idx = 0
        while idx < len(queries):
            resultList.append(retrieveMaxVal(queries[idx]))
            idx += 1

        return resultList