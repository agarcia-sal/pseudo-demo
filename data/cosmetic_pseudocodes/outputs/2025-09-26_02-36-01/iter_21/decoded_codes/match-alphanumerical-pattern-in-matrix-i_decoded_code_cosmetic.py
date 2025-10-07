class Solution:
    def findPattern(self, board, pattern):
        a = len(board)
        b = len(board[0]) if a > 0 else 0
        c = len(pattern)
        d = len(pattern[0]) if c > 0 else 0

        def matches(x, y):
            u = {}
            v = {}
            w = 0
            while w < c:
                x0 = 0
                while x0 < d:
                    y0 = pattern[w][x0]
                    z0 = board[x + w][y + x0]
                    if y0.isdigit():
                        if int(y0) != z0:
                            return False
                    else:
                        if y0 in u:
                            if u[y0] != z0:
                                return False
                        else:
                            if z0 in v:
                                return False
                            u[y0] = z0
                            v[z0] = y0
                    x0 += 1
                w += 1
            return True

        r_temp = 0
        while r_temp <= a - c:
            c_temp = 0
            while c_temp <= b - d:
                if matches(r_temp, c_temp):
                    return [r_temp, c_temp]
                c_temp += 1
            r_temp += 1

        retList = [-1, -1]
        return retList