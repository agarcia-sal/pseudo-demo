class Solution:
    def countOfPairs(self, nums):
        MODULO = 10**9 + 7
        length = len(nums)
        max_num = max(nums) if nums else 0

        dp = [[[0] * (max_num + 1) for _ in range(max_num + 1)] for _ in range(length + 1)]

        first_num = nums[0]
        for a in range(first_num + 1):
            b = first_num - a
            dp[1][a][b] = 1

        for index in range(2, length + 1):
            current = nums[index - 1]
            for x in range(current + 1):
                y = current - x
                # y >= 0 guaranteed by range
                total_sum = 0
                for prev_x in range(x + 1):
                    for prev_y in range(y, max_num + 1):
                        total_sum = (total_sum + dp[index - 1][prev_x][prev_y]) % MODULO
                dp[index][x][y] = total_sum

        total = 0
        for p in range(max_num + 1):
            for q in range(max_num + 1):
                total = (total + dp[length][p][q]) % MODULO

        return total