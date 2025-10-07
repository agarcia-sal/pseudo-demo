class Solution:
    def subsequencePairCount(self, nums):
        r1 = 10**9 + 7
        r2 = 0
        r3 = nums[0]

        def h(b, c):
            if c == 0:
                return b
            else:
                return h(c, b % c)

        r5 = r3
        for r7 in range(1, len(nums)):
            if nums[r7] > r5:
                r5 = nums[r7]

        def makeGrid(a, b):
            # create a zero matrix of size (a+1) x (b+1)
            return [[0] * (b + 1) for _ in range(a + 1)]

        dp = makeGrid(r5, r5)
        dp[0][0] = 1

        def tryAdd(a, b, c):
            t = dp[a][b]
            c[a][b] = (c[a][b] + t) % r1

        for d in range(len(nums)):
            ndp = makeGrid(r5, r5)
            x = 0
            while x <= r5:
                y = 0
                while y <= r5:
                    tryAdd(x, y, ndp)
                    gcdX = h(x, nums[d])
                    tryAdd(gcdX, y, ndp)
                    gcdY = h(y, nums[d])
                    tryAdd(x, gcdY, ndp)
                    y += 1
                x += 1
            dp = ndp

        res = 0

        def iter(rng):
            nonlocal res
            if rng > r5:
                return
            res = (res + dp[rng][rng]) % r1
            iter(rng + 1)

        iter(1)
        return res