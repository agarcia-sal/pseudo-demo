class Solution:
    def maxScore(self, nums):
        length_of_nums = len(nums)
        dp = [0] * length_of_nums
        dp[1] = 0
        outer_index = 2
        while outer_index <= length_of_nums - 1:
            inner_index = 1
            while inner_index < outer_index:
                candidate_value = dp[inner_index] + (outer_index - inner_index) * nums[outer_index]
                if dp[outer_index] < candidate_value:
                    dp[outer_index] = candidate_value
                inner_index += 1
            outer_index += 1
        return dp[length_of_nums - 1]