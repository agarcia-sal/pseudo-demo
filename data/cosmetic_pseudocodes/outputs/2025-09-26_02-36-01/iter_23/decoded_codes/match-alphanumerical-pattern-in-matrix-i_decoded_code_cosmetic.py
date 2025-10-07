class Solution:
    def findPattern(self, board, pattern):
        d1 = len(board)
        d2 = len(board[0])
        q1 = len(pattern)
        q2 = len(pattern[0])

        def matches(x, y):
            mapA = {}
            mapB = {}

            def loopI(m):
                if m == q1:
                    return True

                def loopJ(n):
                    if n == q2:
                        return loopI(m + 1)
                    ch = pattern[m][n]
                    dg = board[x + m][y + n]

                    if '0' <= ch <= '9':
                        if int(ch) != dg:
                            return False
                        return loopJ(n + 1)
                    else:
                        if ch in mapA:
                            if mapA[ch] != dg:
                                return False
                            return loopJ(n + 1)
                        else:
                            if dg in mapB:
                                return False
                            mapA[ch] = dg
                            mapB[dg] = ch
                            return loopJ(n + 1)

                return loopJ(0)

            return loopI(0)

        def loopR(r):
            if r > d1 - q1:
                return [-1, -1]

            def loopC(c):
                if c > d2 - q2:
                    return loopR(r + 1)
                if matches(r, c):
                    return [r, c]
                return loopC(c + 1)

            return loopC(0)

        return loopR(0)