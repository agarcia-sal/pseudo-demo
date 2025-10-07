class Solution:
    def findPattern(self, board, pattern):
        a = len(board)
        b = len(board[0])
        c = len(pattern)
        d = len(pattern[0])

        def matches(x, y):
            m = {}
            n = {}
            for e in range(c):
                for f in range(d):
                    u = pattern[e][f]
                    v = board[x + e][y + f]
                    if '0' <= u <= '9':
                        if int(u) != v:
                            return False
                    else:
                        if u in m:
                            if m[u] != v:
                                return False
                        else:
                            if v in n:
                                return False
                            m[u] = v
                            n[v] = u
            return True

        for i in range(a - c + 1):
            for j in range(b - d + 1):
                if matches(i, j):
                    return [i, j]

        return [-1, -1]