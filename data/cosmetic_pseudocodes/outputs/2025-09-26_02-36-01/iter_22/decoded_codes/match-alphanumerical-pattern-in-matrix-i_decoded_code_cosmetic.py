class Solution:
    def findPattern(self, board, pattern):
        v9 = len(board)
        w0 = len(board[0])
        x3 = len(pattern)
        y7 = len(pattern[0])

        def matches(d1, e2):
            mapA = {}
            mapB = {}

            i4 = 0
            while i4 < x3:
                j5 = 0
                while j5 < y7:
                    chZ = pattern[i4][j5]
                    digY = board[d1 + i4][e2 + j5]

                    if not chZ.isalpha():
                        # chZ expected to be a digit character, match exactly digY
                        if int(chZ) != digY:
                            return False
                    else:
                        # chZ is a letter, must maintain consistent mapping
                        if chZ in mapA:
                            if mapA[chZ] != digY:
                                return False
                        else:
                            if digY in mapB:
                                return False
                            mapA[chZ] = digY
                            mapB[digY] = chZ
                    j5 += 1
                i4 += 1
            return True

        m6 = 0
        while m6 <= v9 - x3:
            n8 = 0
            while n8 <= w0 - y7:
                if matches(m6, n8):
                    return [m6, n8]
                n8 += 1
            m6 += 1

        return [-1, -1]