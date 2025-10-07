from typing import List

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        length = len(nums)
        f_matrix = [[0] * length for _ in range(length)]
        g_matrix = [[0] * length for _ in range(length)]

        for i in range(length - 1, -1, -1):
            f_matrix[i][i] = nums[i]
            g_matrix[i][i] = nums[i]
            for j in range(i + 1, length):
                left_xor = f_matrix[i][j - 1]
                right_xor = f_matrix[i + 1][j]
                f_matrix[i][j] = left_xor ^ right_xor

                val1 = f_matrix[i][j]
                val2 = g_matrix[i][j - 1]
                val3 = g_matrix[i + 1][j]

                max_val = max(val1, val2, val3)
                g_matrix[i][j] = max_val

        results = []
        for l_index, r_index in queries:
            results.append(g_matrix[l_index][r_index])
        return results