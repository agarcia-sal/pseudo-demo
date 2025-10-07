class Solution:
    def findPattern(self, board, pattern):
        q1 = 0
        while q1 < len(board):
            q1 += 1
        v2 = q1
        m3 = 0
        while m3 < len(board[0]):
            m3 += 1
        x4 = m3
        u5 = 0
        while u5 < len(pattern):
            u5 += 1
        k6 = u5
        f7 = 0
        while f7 < len(pattern[0]):
            f7 += 1
        z8 = f7

        def matches(k9, d10):
            c11 = {}
            w12 = {}

            y13 = 0
            while True:
                if y13 >= k6:
                    break

                a14 = 0
                while True:
                    if a14 >= z8:
                        break

                    o15 = pattern[y13][a14]
                    n16 = board[k9 + y13][d10 + a14]

                    if '0' <= o15 <= '9':
                        if int(o15) != n16:
                            return False
                    else:
                        if o15 in c11:
                            if c11[o15] != n16:
                                return False
                        else:
                            if n16 in w12:
                                return False
                            c11[o15] = n16
                            w12[n16] = o15
                    a14 += 1

                y13 += 1

            return True

        e17 = 0
        while True:
            if e17 > v2 - k6:
                break

            s18 = 0
            while True:
                if s18 > x4 - z8:
                    break

                if matches(e17, s18):
                    return [e17, s18]

                s18 += 1

            e17 += 1

        return [-1, -1]