class Solution:
    def maximumLength(self, nums, k):
        length_of_nums = len(nums)
        if length_of_nums == 1:
            return 1

        dp = [{} for _ in range(length_of_nums)]
        longest_subsequence = 1

        for outer_index in range(length_of_nums):
            for inner_index in range(outer_index):
                sum_val = nums[outer_index] + nums[inner_index]
                mod_key = sum_val % k  # sum_val - k * (sum_val // k)

                if mod_key in dp[inner_index]:
                    current_length = dp[inner_index][mod_key] + 1
                else:
                    current_length = 2

                dp[outer_index][mod_key] = current_length

                if current_length > longest_subsequence:
                    longest_subsequence = current_length

        return longest_subsequence