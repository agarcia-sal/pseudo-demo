class Solution:
    def findPattern(self, board, pattern):
        M = len(board)
        N = len(board[0]) if M > 0 else 0
        R = len(pattern)
        S = len(pattern[0]) if R > 0 else 0

        def matches(x, y):
            mapC = {}
            mapD = {}

            def eqDigit(ch):
                return '0' <= ch <= '9'

            idx1 = 0
            while idx1 < R:
                idx2 = 0
                while idx2 < S:
                    patCh = pattern[idx1][idx2]
                    bdVal = board[x + idx1][y + idx2]

                    if eqDigit(patCh):
                        if bdVal != int(patCh):
                            return False
                    else:
                        if patCh in mapC:
                            if mapC[patCh] != bdVal:
                                return False
                        else:
                            if bdVal in mapD:
                                return False
                            mapC[patCh] = bdVal
                            mapD[bdVal] = patCh

                    idx2 += 1
                idx1 += 1
            return True

        r1 = 0
        while r1 <= M - R:
            c1 = 0
            while c1 <= N - S:
                if matches(r1, c1):
                    return [r1, c1]
                c1 += 1
            r1 += 1

        return [-1, -1]