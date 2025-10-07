class Solution:
    def countOfPairs(self, nums):
        MOD = 10**9 + 7
        size = len(nums)
        highestVal = max(nums)

        # Initialize dp as a 3D list: dp[size][highestVal + 1][highestVal + 1], all zeros
        dp = [[[0] * (highestVal + 1) for _ in range(highestVal + 1)] for _ in range(size)]

        firstNum = nums[0]
        for var_j in range(firstNum + 1):
            var_k = firstNum - var_j
            dp[0][var_j][var_k] = 1

        for i in range(1, size):
            currentNum = nums[i]
            for j_loop in range(currentNum + 1):
                k_loop = currentNum - j_loop
                for j_prev_loop in range(j_loop + 1):
                    for k_prev_loop in range(k_loop, highestVal + 1):
                        dp[i][j_loop][k_loop] = (dp[i][j_loop][k_loop] + dp[i - 1][j_prev_loop][k_prev_loop]) % MOD

        finalResult = 0
        lastNum = nums[size - 1]
        for j_sum in range(highestVal + 1):
            for k_sum in range(highestVal + 1):
                if (j_sum + k_sum) == lastNum:
                    finalResult = (finalResult + dp[size - 1][j_sum][k_sum]) % MOD

        return finalResult