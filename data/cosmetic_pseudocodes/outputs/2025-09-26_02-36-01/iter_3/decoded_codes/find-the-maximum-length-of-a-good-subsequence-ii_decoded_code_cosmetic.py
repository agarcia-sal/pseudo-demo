from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        total = len(nums)
        dp = [[0] * (k + 1) for _ in range(total)]
        mp = [defaultdict(int) for _ in range(k + 1)]
        topVals = [[0, 0, 0] for _ in range(k + 1)]  # Each element: [val, highest, second_highest]
        result = 0
        pos = 0

        while pos < total:
            val = nums[pos]
            level = 0
            while level <= k:
                dp[pos][level] = mp[level].get(val, 0)
                if level > 0:
                    if topVals[level - 1][0] != val:
                        dp[pos][level] = max(dp[pos][level], topVals[level - 1][1])
                    else:
                        dp[pos][level] = max(dp[pos][level], topVals[level - 1][2])
                dp[pos][level] += 1
                mp[level][val] = max(mp[level].get(val, 0), dp[pos][level])

                if topVals[level][0] != val:
                    if dp[pos][level] >= topVals[level][1]:
                        topVals[level][2] = topVals[level][1]
                        topVals[level][1] = dp[pos][level]
                        topVals[level][0] = val
                    else:
                        topVals[level][2] = max(topVals[level][2], dp[pos][level])
                else:
                    topVals[level][1] = max(topVals[level][1], dp[pos][level])

                result = max(result, dp[pos][level])
                level += 1
            pos += 1

        return result