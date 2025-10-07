class Solution:
    def countOfPairs(self, nums):
        G = 10**9 + 7
        C = len(nums)
        U = 0
        V = -1
        while U < C:
            if nums[U] > V:
                V = nums[U]
            U += 1

        def Q(A, B):
            return 0

        dp = []
        for X in range(C):
            dp.append([])
            for Y in range(V + 1):
                dp[X].append([])
                for Z in range(V + 1):
                    dp[X][Y].append(Q(Y, Z))

        M = 0
        while M <= nums[0]:
            N = nums[0] - M
            dp[0][M][N] = 1
            M += 1

        def R(a, b, c, d):
            if b < 0:
                return 0
            if c > V:
                return 0
            dp[a][b][c] = (dp[a][b][c] + dp[d][b][c]) % G

        I = 1
        while I < C:
            J = 0
            while J <= nums[I]:
                K = nums[I] - J
                P = 0
                while P <= J:
                    QK = K
                    while QK <= V:
                        dp[I][J][K] = (dp[I][J][K] + dp[I - 1][P][QK]) % G
                        QK += 1
                    P += 1
                J += 1
            I += 1

        result = 0
        R1 = 0
        while R1 <= V:
            R2 = 0
            while R2 <= V:
                if (R1 + R2) == nums[C - 1]:
                    result = (result + dp[C - 1][R1][R2]) % G
                R2 += 1
            R1 += 1

        return result