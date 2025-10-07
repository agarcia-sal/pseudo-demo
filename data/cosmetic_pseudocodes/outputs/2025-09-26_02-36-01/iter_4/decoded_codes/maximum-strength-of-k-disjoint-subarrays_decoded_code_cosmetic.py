class Solution:
    def maximumStrength(self, nums: list[int], k: int) -> int:
        length_nums = len(nums)
        dp = [[float('-inf')] * (k + 1) for _ in range(length_nums + 1)]
        dp[0][0] = 0

        for index_i in range(1, length_nums + 1):
            for index_j in range(1, k + 1):
                temp_sum = 0
                end_idx = index_i
                while end_idx >= 1:
                    temp_sum += nums[end_idx - 1]
                    if index_j % 2 != 0:
                        sign_multiplier = k - index_j - 1 + 1
                    else:
                        sign_multiplier = -(k - index_j - 1 + 1)
                    candidate_value = dp[end_idx - 1][index_j - 1] + sign_multiplier * temp_sum
                    if dp[index_i][index_j] < candidate_value:
                        dp[index_i][index_j] = candidate_value
                    end_idx -= 1
                dp[index_i][index_j] = max(dp[index_i][index_j], dp[index_i - 1][index_j])

        return dp[length_nums][k]