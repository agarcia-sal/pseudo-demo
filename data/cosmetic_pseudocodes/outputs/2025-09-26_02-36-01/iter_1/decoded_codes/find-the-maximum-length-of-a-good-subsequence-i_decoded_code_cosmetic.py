class Solution:
    def maximumLength(self, nums, k):
        n = len(nums)
        f = [[1] * (k + 1) for _ in range(n)]
        ans = 0
        for i in range(n):
            x = nums[i]
            for h in range(k + 1):
                for j in range(i):
                    y = nums[j]
                    if x == y:
                        f[i][h] = max(f[i][h], f[j][h] + 1)
                    elif h > 0:
                        f[i][h] = max(f[i][h], f[j][h - 1] + 1)
            ans = max(ans, f[i][k])
        return ans