class Solution:
    def countOfPairs(self, nums):
        modulus = 10**9 + 7
        length_nums = len(nums)
        highest_val = max(nums)

        # dp_array[i][j][k]: number of ways to form the first i numbers where
        # the sum split is j for one part and k for the other, with j + k = current_value
        dp_array = [[[0] * (highest_val + 1) for _ in range(highest_val + 1)] for _ in range(length_nums + 1)]

        initial_num = nums[0]
        for idx_j in range(initial_num + 1):
            dp_array[1][idx_j][initial_num - idx_j] = 1

        for idx_i in range(2, length_nums + 1):
            current_value = nums[idx_i - 1]
            for idx_j_inner in range(current_value + 1):
                for idx_k_inner in range(current_value + 1):
                    if idx_j_inner + idx_k_inner == current_value:
                        total = 0
                        for prev_j_idx in range(idx_j_inner + 1):
                            # We sum over prev_k_idx from idx_k_inner up to highest_val
                            for prev_k_idx in range(idx_k_inner, highest_val + 1):
                                total += dp_array[idx_i - 1][prev_j_idx][prev_k_idx]
                        dp_array[idx_i][idx_j_inner][idx_k_inner] = total % modulus

        total_result = 0
        for final_j in range(highest_val + 1):
            for final_k in range(highest_val + 1):
                total_result = (total_result + dp_array[length_nums][final_j][final_k]) % modulus

        return total_result