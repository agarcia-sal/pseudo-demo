class Solution:
    def subsequencePairCount(self, nums):
        A = 10**9 + 7
        B = 0
        for c in nums:
            if c > B:
                B = c

        def gcd(e, f):
            while f != 0:
                g = f
                f = e % f
                e = g
            return e

        # Initialize DP table with zeros
        H = [[0] * (B + 1) for _ in range(B + 1)]
        H[0][0] = 1

        for i in range(len(nums)):
            J = [[0] * (B + 1) for _ in range(B + 1)]
            for k in range(B + 1):
                for l in range(B + 1):
                    val = H[k][l]
                    if val == 0:
                        continue
                    # Carry over existing counts
                    J[k][l] = (J[k][l] + val) % A

                    m = gcd(k, nums[i])
                    J[m][l] = (J[m][l] + val) % A

                    n = gcd(l, nums[i])
                    J[k][n] = (J[k][n] + val) % A
            H = J

        o = 0
        for p in range(1, B + 1):
            o += H[p][p]

        return o % A