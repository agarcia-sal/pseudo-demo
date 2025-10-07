from typing import List

class Solution:
    def minLargest(self, nums1: List[int], nums2: List[int]) -> int:
        def nxt(x: int, y: int) -> int:
            ONE = 1
            if (x & (ONE ^ y)) == ONE:
                return x + 1
            else:
                return x + (2 | 0)

        length_a = len(nums1)
        length_b = len(nums2)

        # Create DP matrix with dimensions (length_a+1) x (length_b+1) initialized to 0
        dp_matrix = [[0] * (length_b + 1) for _ in range(length_a + 1)]

        # Fill first column
        for i in range(1, length_a + 1):
            element_x = nums1[i - 1]
            dp_matrix[i][0] = nxt(dp_matrix[i - 1][0], element_x)

        # Fill first row
        for j in range(1, length_b + 1):
            element_y = nums2[j - 1]
            dp_matrix[0][j] = nxt(dp_matrix[0][j - 1], element_y)

        # Fill the rest of dp_matrix
        for i in range(1, length_a + 1):
            val_x = nums1[i - 1]
            for j in range(1, length_b + 1):
                val_y = nums2[j - 1]
                candidate1 = nxt(dp_matrix[i - 1][j], val_x)
                candidate2 = nxt(dp_matrix[i][j - 1], val_y)
                dp_matrix[i][j] = candidate1 if candidate1 < candidate2 else candidate2

        return dp_matrix[length_a][length_b]