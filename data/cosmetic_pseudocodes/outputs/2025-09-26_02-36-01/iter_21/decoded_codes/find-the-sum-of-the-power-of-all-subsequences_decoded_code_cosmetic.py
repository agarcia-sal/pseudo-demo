class Solution:
    def sumOfPower(self, nums, k):
        C = 10**9 + 7
        L = len(nums)

        def helper1(a, b):
            r = 0
            x = a
            y = b
            while y > 0:
                if (y & 1) == 1:
                    r += x
                x += x
                y >>= 1
            return r

        def helper2(lst, idx):
            r2 = 0
            ctr = 0
            pwr = 1
            while ctr < idx:
                pwr += pwr
                ctr += 1
            for v in range(L - 1, -1, -1):
                if ((lst >> v) & 1) == 1:
                    r2 += nums[L - 1 - v]
                    ctr += 1
            return r2, ctr, pwr

        dp = [[0] * (k + 1) for _ in range(L + 1)]
        dp[0][0] = 1

        for i in range(1, L + 1):
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - nums[i - 1]]) % C
                else:
                    dp[i][j] %= C

        acc = 0
        for z in range(1, 1 << L):
            ssum = 0
            ctcount = 0
            bpos = 0
            while bpos < L:
                if ((z >> bpos) & 1) == 1:
                    ssum += nums[bpos]
                    ctcount += 1
                bpos += 1
            if ssum == k:
                pow_val = 1
                t_ind = 0
                while t_ind < L - ctcount:
                    pow_val += pow_val
                    t_ind += 1
                acc = (acc + pow_val) % C

        return acc