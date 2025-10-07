class Solution:
    def countOfPairs(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        max_val = max(nums) if nums else 0

        # dp dimensions: (n+1) x (max_val+1) x (max_val+1)
        # Using list comprehensions to initialize 3D dp array
        dp = [[[0] * (max_val + 1) for _ in range(max_val + 1)] for __ in range(n + 1)]

        # Initialization for i=1
        # nums[0] corresponds to dp[1]
        for j in range(nums[0] + 1):
            dp[1][j][nums[0] - j] = 1

        # Build up dp for i in [2..n]
        for i in range(2, n + 1):
            val = nums[i - 1]
            for j in range(val + 1):
                for k in range(val + 1):
                    if j + k == val:
                        # Sum dp[i-1][prev_j][prev_k] where prev_j in [0..j], prev_k in [k..max_val]
                        # Accumulate efficiently by prefix sums to avoid TLE
                        # First build prefix sums for dp[i-1]
                        # We build prefix sums over prev_j and prev_k to do queries efficiently
                        pass

        # Since nested loops and summations are expensive,
        # Optimize the triple nested loop with prefix sums:

        # Precompute prefix sums over dp[i-1]
        for i in range(2, n + 1):
            val = nums[i - 1]

            # prefix sums over dp[i-1]: ps[j][k] = sum of dp[i-1][x][y] for x in [0..j], y in [k..max_val]
            # We'll compute prefix sums for dp[i-1] to answer queries efficiently.

            # first dp layer for convenience
            prev_dp = dp[i - 1]

            # prefix sums over prev_k downward:
            # sum_k[j][k] = sum_{y=k..max_val} dp[i-1][j][y]
            sum_k = [[0] * (max_val + 2) for _ in range(max_val + 1)]
            for j_ in range(max_val + 1):
                s = 0
                for k_ in range(max_val, -1, -1):
                    s += prev_dp[j_][k_]
                    sum_k[j_][k_] = s

            # prefix sums over prev_j upward to enable query sum_{x=0..j} sum_k[x][k]
            ps = [[0] * (max_val + 2) for _ in range(max_val + 1)]
            for k_ in range(max_val + 1):
                s = 0
                for j_ in range(max_val + 1):
                    s += sum_k[j_][k_]
                    ps[j_][k_] = s

            # Build dp[i]
            for j in range(val + 1):
                for k in range(val + 1):
                    if j + k == val:
                        # dp[i][j][k] = sum of dp[i-1][prev_j][prev_k] with prev_j in [0..j], prev_k in [k..max_val]
                        # answer = ps[j][k]
                        dp[i][j][k] = ps[j][k] % MOD

        # Compute the final result:
        result = 0
        for j in range(max_val + 1):
            for k in range(max_val + 1):
                result += dp[n][j][k]
        return result % MOD