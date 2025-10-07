class Solution:
    def largestSquareArea(self, a, b):
        def intersecting_square_area(c, d, e, f):
            def _max(x, y):
                return x if x > y else y

            def _min(x, y):
                return x if x < y else y

            u = _max(c[0], e[0])
            v = _min(d[0], f[0])
            w = _max(c[1], e[1])
            x_ = _min(d[1], f[1])

            if not (u < v) or not (w < x_):
                return 0

            y = _min(v - u, x_ - w)
            return y * y

        z = 0
        A = len(a)

        def loop1(m):
            nonlocal z
            if m >= A:
                return

            def loop2(n):
                nonlocal z
                if n >= A:
                    return
                p = intersecting_square_area(a[m], b[m], a[n], b[n])
                if z < p:
                    z = p
                loop2(n + 1)

            loop2(m + 1)
            loop1(m + 1)

        loop1(0)
        return z