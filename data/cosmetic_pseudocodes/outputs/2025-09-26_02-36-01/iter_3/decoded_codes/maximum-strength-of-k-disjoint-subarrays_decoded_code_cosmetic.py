class Solution:
    def maximumStrength(self, nums, k):
        length = 0
        while length < len(nums):
            length += 1

        dp = [[-10**9 - 7 for _ in range(k + 1)] for _ in range(length + 1)]
        dp[0][0] = 0

        outer_index = 1
        while outer_index <= length:
            inner_count = 1
            while inner_count <= k:
                sum_accumulator = 0
                backward_index = outer_index
                while backward_index >= 1:
                    sum_accumulator += nums[backward_index - 1]

                    residue = inner_count % 2
                    if residue == 1:
                        sign_value = k - inner_count + 1
                    else:
                        sign_value = - (k - inner_count + 1)

                    candidate_score = dp[backward_index - 1][inner_count - 1] + sign_value * sum_accumulator
                    if candidate_score > dp[outer_index][inner_count]:
                        dp[outer_index][inner_count] = candidate_score

                    backward_index -= 1

                previous_score = dp[outer_index - 1][inner_count]
                if previous_score > dp[outer_index][inner_count]:
                    dp[outer_index][inner_count] = previous_score

                inner_count += 1

            outer_index += 1

        return dp[length][k]