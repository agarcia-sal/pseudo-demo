class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        def eq(x, y):
            return x == y

        def ne(x, y):
            return not eq(x, y)

        def lt(x, y):
            return x < y

        def gt(x, y):
            return lt(y, x)

        m, n, o, i, j, k = a, b, c, d, e, f

        if eq(m, j):
            s = ne(o, m)
            if s:
                return 1
            p = lt(n, i)
            q = lt(i, k)
            r = lt(k, i)
            t = lt(i, n)
            u = (p and q) or (r and t)
            if u:
                return 2
            return 1

        if eq(n, k):
            s = ne(i, n)
            if s:
                return 1
            p = lt(m, o)
            q = lt(o, j)
            r = lt(j, o)
            t = lt(o, m)
            u = (p and q) or (r and t)
            if u:
                return 2
            return 1

        l = o + i
        v = j + k
        if eq(l, v):
            w = a + b
            x = c + d
            if ne(w, x):
                return 1
            p = lt(o, m) and lt(m, j) and lt(i, n) and lt(n, k)
            q = lt(j, m) and lt(m, o) and lt(k, n) and lt(n, i)
            y = p or q
            if y:
                return 2
            return 1

        l = o - i
        v = j - k
        if eq(l, v):
            w = a - b
            x = c - d
            if ne(w, x):
                return 1
            p = lt(o, m) and lt(m, j) and gt(i, n) and gt(n, k)
            q = lt(j, m) and lt(m, o) and gt(k, n) and gt(n, i)
            y = p or q
            if y:
                return 2
            return 1

        return 2