class Solution:
    def findPattern(self, board, pattern):
        α = len(board)
        β = len(board[0]) if α > 0 else 0
        γ = len(pattern)
        δ = len(pattern[0]) if γ > 0 else 0

        def matches(x, y):
            Ω = {}
            Σ = {}

            def isDigit(ch):
                return '0' <= ch <= '9'

            m = 0
            while m <= γ - 1:
                n = 0
                while n <= δ - 1:
                    u = pattern[m]
                    v = u[n]
                    w = board[x + m]
                    z = w[y + n]

                    if isDigit(v):
                        if int(v) != z:
                            return False
                    else:
                        if v in Ω:
                            if Ω[v] != z:
                                return False
                        else:
                            if z in Σ:
                                return False
                            Ω[v] = z
                            Σ[z] = v
                    n += 1
                m += 1
            return True

        i = 0
        while i <= α - γ:
            j = 0
            while j <= β - δ:
                if matches(i, j):
                    return [i, j]
                j += 1
            i += 1
        return [-1, -1]