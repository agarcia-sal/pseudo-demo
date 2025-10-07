from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        length_of_nums = len(nums)
        if length_of_nums == 1:
            return 1

        dp = [defaultdict(int) for _ in range(length_of_nums)]
        final_result = 1

        def recurse_outer(m):
            if m >= length_of_nums:
                return
            idx_inner = 0

            def recurse_inner(n):
                if n >= m:
                    return
                sum_mod = (nums[m] + nums[n]) % k
                if sum_mod in dp[n]:
                    dp[m][sum_mod] = dp[n][sum_mod] + 1
                else:
                    dp[m][sum_mod] = 2  # 1 + 1 from pseudocode
                nonlocal final_result
                if dp[m][sum_mod] > final_result:
                    final_result = dp[m][sum_mod]
                recurse_inner(n + 1)

            recurse_inner(idx_inner)
            recurse_outer(m + 1)

        recurse_outer(0)
        return final_result