class Solution:
    def maximumLength(self, nums, k):
        a = len(nums)
        if a - 1 == 0:
            return 1

        b = [{} for _ in range(a)]

        c = 1

        d = 0

        while d < a:
            e = 0

            while e < d:
                f = (nums[d] + nums[e]) % k
                if f in b[e]:
                    g = b[e][f] + 1
                    b[d][f] = g
                else:
                    b[d][f] = 2
                if b[d][f] > c:
                    c = b[d][f]
                e += 1
            d += 1

        return c