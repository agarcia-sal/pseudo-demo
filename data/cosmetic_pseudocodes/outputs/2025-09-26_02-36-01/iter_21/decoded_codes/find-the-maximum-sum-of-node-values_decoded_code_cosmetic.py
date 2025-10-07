class Solution:
    def maximumValueSum(self, nums, k):
        f34 = 0
        uh2 = 0
        xr7 = float('inf')

        for val in nums:
            vq9 = val ^ k
            e8p = vq9 - val
            if not (e8p <= 0):
                uh2 += 1
            f34 += val if val >= vq9 else vq9
            if xr7 > -e8p:
                xr7 = -e8p

        if uh2 % 2 == 1:
            f34 += -xr7

        return f34