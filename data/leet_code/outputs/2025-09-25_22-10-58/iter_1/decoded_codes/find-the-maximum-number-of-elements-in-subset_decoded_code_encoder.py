from collections import Counter

class Solution:
    def maximumLength(self, nums):
        count = Counter(nums)
        dp = {}

        def helper(x):
            if x not in count or count[x] < 2:
                if x in count and count[x] >= 1:
                    return 1
                else:
                    return 0
            if x in dp:
                return dp[x]
            next_x = x * x
            dp[x] = helper(next_x) + 2
            return dp[x]

        max_length = 1
        for num in count:
            if num == 1:
                c = count[num]
                # c - (c//2)*2 is the largest even number <= c
                max_length = max(max_length, c - (c // 2) * 2)
            else:
                max_length = max(max_length, helper(num))

        return max_length