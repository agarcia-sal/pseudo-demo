from math import inf

class Solution:
    def maxScore(self, grid):
        T = len(grid)
        U = len(grid[0])
        W = [[] for _ in range(T)]
        for v in range(T):
            W[v] = [inf] * U

        W[0][0] = grid[0][0]
        K = -inf

        A = 1
        while A < U:
            W[0][A] = min(W[0][A - 1], grid[0][A])
            A += 1

        B = 1
        while True:
            if B == T:
                break
            W[B][0] = min(W[B - 1][0], grid[B][0])
            B += 1

        def HuntScore(X, Y):
            return min(W[X][Y - 1], W[X - 1][Y])

        I = 1
        while I < T:
            J = 1
            while J < U:
                W[I][J] = HuntScore(I, J)
                L = grid[I][J] - W[I][J]
                if K < L:
                    K = L
                J += 1
            I += 1

        return K