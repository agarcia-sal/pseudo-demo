class Solution:
    def sumOfPower(self, nums, k):
        mod = 10**9 + 7
        n = len(nums)

        # Initialize dp as a list of lists with zeros
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # base case

        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - num]) % mod
                else:
                    dp[i][j] %= mod

        result = 0
        full_mask = (1 << n) - 1

        # Precompute nums to avoid multiple indexing in bit iterations
        nums_arr = nums

        # Since n can be up to reasonable limits, process all subsets by bitmasking
        # Using iterative approach instead of recursion for performance and clarity
        for mask in range(1, full_mask + 1):
            sum_selected = 0
            selected_count = 0

            # Check bits of mask
            m = mask
            idx = 0
            while m > 0:
                if m & 1:
                    sum_selected += nums_arr[idx]
                    selected_count += 1
                idx += 1
                m >>= 1

            if sum_selected == k:
                result = (result + (1 << (n - selected_count))) % mod

        return result