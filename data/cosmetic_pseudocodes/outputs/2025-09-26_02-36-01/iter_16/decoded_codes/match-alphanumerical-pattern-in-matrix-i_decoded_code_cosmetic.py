class Solution:
    def findPattern(self, board, pattern):
        A = len(board)
        B = len(board[0])
        C = len(pattern)
        D = len(pattern[0])

        def matches(X, Y):
            M = {}
            N = {}
            for U in range(C):
                for V in range(D):
                    W = pattern[U][V]
                    Z = board[X + U][Y + V]
                    if '0' <= W <= '9':
                        if int(W) != Z:
                            return False
                    else:
                        if W in M:
                            if M[W] != Z:
                                return False
                        else:
                            if Z in N:
                                return False
                            M[W] = Z
                            N[Z] = W
            return True

        for i in range(A - C + 1):
            for j in range(B - D + 1):
                if matches(i, j):
                    return [i, j]
        return [-1, -1]