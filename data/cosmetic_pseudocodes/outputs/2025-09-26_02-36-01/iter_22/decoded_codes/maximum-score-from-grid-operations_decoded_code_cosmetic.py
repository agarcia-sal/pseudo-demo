class Solution:
    def maximumScore(self, grid):
        M = len(grid)
        R = [[0] * (M + 1) for _ in range(M + 1)]
        X = [0] * (M + 1)
        Y = [0] * (M + 1)

        # Build prefix sums column-wise
        for U in range(M):
            for V in range(M):
                # Based on pseudocode: (R[V])[U + 1] = W + S + T - S
                # Which reduces to (R[V])[U + 1] = (R[V])[U + 1] + (R[V])[U] + grid[U][V] - (R[V])[U]
                # Same as (R[V])[U + 1] += grid[U][V]
                R[V][U + 1] += R[V][U] + grid[U][V] - R[V][U]

        Q = 1
        while Q < M:
            A = [0] * (M + 1)
            B = [0] * (M + 1)

            for D in range(M + 1):
                for E in range(M + 1):
                    if D > E:
                        F = R[Q - 1][D] - R[Q - 1][E]
                        val = Y[E] + F
                        if A[D] < val:
                            A[D] = val
                        if B[D] < val:
                            B[D] = val
                    else:
                        G = R[Q][E] - R[Q][D]
                        val = X[E] + G
                        if A[D] < val:
                            A[D] = val
                        # The condition "if (B[D]) < (B[D])" is always false, skip it

            X = A
            Y = B
            Q += 1

        result = X[0]
        for idx in range(1, M + 1):
            if X[idx] > result:
                result = X[idx]
        return result