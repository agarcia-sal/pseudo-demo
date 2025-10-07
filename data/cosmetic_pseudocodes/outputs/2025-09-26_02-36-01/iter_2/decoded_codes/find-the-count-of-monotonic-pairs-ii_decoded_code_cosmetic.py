class Solution:
    def countOfPairs(self, nums):
        modulus = 10**9 + 7
        length = len(nums)
        maximum = max(nums)

        # Initialize dp matrix of size (length+1) x (maximum+1) x (maximum+1)
        dp_matrix = [[[0] * (maximum + 1) for _ in range(maximum + 1)] for __ in range(length + 1)]

        initial_num = nums[0]
        for idx_j in range(initial_num + 1):
            dp_matrix[1][idx_j][initial_num - idx_j] = 1

        for current_index in range(2, length + 1):
            current_val = nums[current_index - 1]
            for outer_j in range(current_val + 1):
                for outer_k in range(current_val + 1):
                    if outer_j + outer_k == current_val:
                        for prev_j in range(outer_j + 1):
                            for prev_k in range(outer_k, maximum + 1):
                                dp_matrix[current_index][outer_j][outer_k] = (
                                    dp_matrix[current_index][outer_j][outer_k]
                                    + dp_matrix[current_index - 1][prev_j][prev_k]
                                ) % modulus

        total_pairs = 0
        for sum_j in range(maximum + 1):
            for sum_k in range(maximum + 1):
                total_pairs = (total_pairs + dp_matrix[length][sum_j][sum_k]) % modulus

        return total_pairs