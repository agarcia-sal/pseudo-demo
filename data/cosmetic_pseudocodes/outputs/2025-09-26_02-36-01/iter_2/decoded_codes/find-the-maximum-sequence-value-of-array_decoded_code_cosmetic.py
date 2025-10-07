class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        limit = 1 << 7
        length = len(nums)
        # dp[i][j][mask] indicates if it's possible to pick j elements from first i elements with OR mask = mask
        dp = [[[False] * limit for _ in range(k + 2)] for _ in range(length + 1)]
        dp[0][0][0] = True

        for i in range(length):
            for j in range(k + 1):
                for mask in range(limit):
                    if dp[i][j][mask]:
                        # Not pick nums[i]
                        dp[i + 1][j][mask] = True
                        # Pick nums[i]
                        if j + 1 <= k + 1:
                            dp[i + 1][j + 1][mask | nums[i]] = True

        # dp_backward[i][j][mask] indicates if it's possible to pick j elements from last (length - i) elements with OR mask = mask
        dp_backward = [[[False] * limit for _ in range(k + 2)] for _ in range(length + 1)]
        dp_backward[length][0][0] = True

        for i_down in range(length, 0, -1):
            for j in range(k + 1):
                for mask in range(limit):
                    if dp_backward[i_down][j][mask]:
                        # Not pick nums[i_down - 1]
                        dp_backward[i_down - 1][j][mask] = True
                        # Pick nums[i_down - 1]
                        if j + 1 <= k + 1:
                            dp_backward[i_down - 1][j + 1][mask | nums[i_down - 1]] = True

        max_result = 0
        # position iterates from k to length - k inclusive
        for position in range(k, length - k + 1):
            for mask_x in range(limit):
                if dp[position][k][mask_x]:
                    for mask_y in range(limit):
                        if dp_backward[position][k][mask_y]:
                            xor_val = mask_x ^ mask_y
                            if xor_val > max_result:
                                max_result = xor_val

        return max_result