class Solution:
    def sumOfPower(self, nums: list[int], k: int) -> int:
        R = 10**9 + 7
        c = len(nums)
        Q = [[0] * (k + 1) for _ in range(c + 1)]
        Q[0][0] = 1

        for u in range(1, c + 1):
            for v in range(k + 1):
                Q[u][v] = Q[u - 1][v]
                if v >= nums[u - 1]:
                    Q[u][v] += Q[u - 1][v - nums[u - 1]]
                Q[u][v] %= R

        W = 0
        m = (1 << c) - 1  # 2^c - 1

        for x in range(1, m + 1):
            A = 0
            B = 0
            for y in range(c):
                if (x >> y) & 1:
                    A += nums[y]
                    B += 1
            if A == k:
                W += (1 << (c - B))
                W %= R

        return W