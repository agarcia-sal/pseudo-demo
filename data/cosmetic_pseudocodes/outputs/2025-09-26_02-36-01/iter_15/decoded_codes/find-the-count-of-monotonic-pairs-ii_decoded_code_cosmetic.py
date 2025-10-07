class Solution:
    def countOfPairs(self, nums):
        const_val = 10**9 + 7
        size_m = len(nums)
        max_element = max(nums)

        # Initialize the 3D DP table with zeros
        table = [[[0] * (max_element + 1) for _ in range(max_element + 1)] for __ in range(size_m + 1)]

        # Base case initialization for the first element
        for idx_b in range(nums[0] + 1):
            table[1][idx_b][nums[0] - idx_b] = 1

        # Fill DP table for elements 2 to size_m
        for outer_i in range(2, size_m + 1):
            limit_j = nums[outer_i - 1]
            for middle_j in range(limit_j + 1):
                for inner_k in range(limit_j + 1):
                    if middle_j + inner_k == nums[outer_i - 1]:
                        for p_j in range(middle_j + 1):
                            p_k = middle_j + inner_k - p_j
                            if p_k <= max_element:
                                table[outer_i][middle_j][inner_k] += table[outer_i - 1][p_j][p_k]
                                table[outer_i][middle_j][inner_k] %= const_val

        # Compute final answer by summing all possible pairs for last element
        answer = 0
        for first_j in range(max_element + 1):
            for first_k in range(max_element + 1):
                answer += table[size_m][first_j][first_k]
        return answer % const_val