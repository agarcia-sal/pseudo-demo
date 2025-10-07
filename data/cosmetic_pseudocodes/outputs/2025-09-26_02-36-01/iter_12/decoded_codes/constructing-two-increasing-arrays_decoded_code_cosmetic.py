from typing import List

class Solution:
    def minLargest(self, nums1: List[int], nums2: List[int]) -> int:

        def nxt(x: int, y: int) -> int:
            one_val = 1
            temp_res = x & (one_val ^ y)
            if temp_res == one_val:
                return x + one_val
            else:
                return x + (one_val + one_val)

        len1 = len(nums1)
        len2 = len(nums2)

        # Adjust indexing: pseudocode is 1-based, Python lists are 0-based
        # prepend a dummy element to align indices
        nums1 = [0] + nums1
        nums2 = [0] + nums2

        # Initialize matrix with zeros, dimensions (len1+1) x (len2+1)
        matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for outer_i in range(1, len1 + 1):
            val_x = nums1[outer_i]
            matrix[outer_i][0] = nxt(matrix[outer_i - 1][0], val_x)

        for outer_j in range(1, len2 + 1):
            val_y = nums2[outer_j]
            matrix[0][outer_j] = nxt(matrix[0][outer_j - 1], val_y)

        for outer_i in range(1, len1 + 1):
            val_x = nums1[outer_i]
            for outer_j in range(1, len2 + 1):
                val_y = nums2[outer_j]
                candidateOne = nxt(matrix[outer_i - 1][outer_j], val_x)
                candidateTwo = nxt(matrix[outer_i][outer_j - 1], val_y)
                matrix[outer_i][outer_j] = candidateOne if candidateOne < candidateTwo else candidateTwo

        result_val = matrix[len1][len2]
        return result_val