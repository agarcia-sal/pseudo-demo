class Solution:
    def countOfPairs(self, nums):
        A = 10**9 + 7
        B = len(nums)
        C = nums[0]
        for D in range(1, B):
            if nums[D] > C:
                C = nums[D]

        E = []
        for F in range(B):
            G = []
            for H in range(C + 1):
                G.append([0] * (C + 1))
            E.append(G)

        for I in range(nums[0] + 1):
            J = nums[0] - I
            E[0][I][J] = 1

        K = 1
        while K < B:
            L = nums[K]
            M = 0
            while M <= L:
                N = L - M
                O = 0
                while O <= M:
                    P = N
                    while P <= C:
                        Q = E[K][M][N] + E[K - 1][O][P]
                        E[K][M][N] = Q % A
                        P += 1
                    O += 1
                M += 1
            K += 1

        R = 0
        S = B - 1
        T = nums[S]
        for U in range(C + 1):
            for V in range(C + 1):
                if U + V == T:
                    R = (R + E[S][U][V]) % A

        return R