from typing import List

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        alpha = len(nums)
        beta = [[0]*alpha for _ in range(alpha)]
        gamma = [[0]*alpha for _ in range(alpha)]

        vec1 = alpha - 1
        while vec1 >= 0:
            beta[vec1][vec1] = nums[vec1]
            gamma[vec1][vec1] = nums[vec1]
            vec2 = vec1 + 1
            while vec2 < alpha:
                tmp1 = beta[vec1][vec2 - 1] ^ beta[vec1 + 1][vec2]
                beta[vec1][vec2] = tmp1
                tmp2 = max(beta[vec1][vec2], gamma[vec1][vec2 - 1], gamma[vec1 + 1][vec2])
                gamma[vec1][vec2] = tmp2
                vec2 += 1
            vec1 -= 1

        resultList = []
        idx = 0
        while idx < len(queries):
            l_val = queries[idx][0]
            r_val = queries[idx][1]
            resultList.append(gamma[l_val][r_val])
            idx += 1

        return resultList