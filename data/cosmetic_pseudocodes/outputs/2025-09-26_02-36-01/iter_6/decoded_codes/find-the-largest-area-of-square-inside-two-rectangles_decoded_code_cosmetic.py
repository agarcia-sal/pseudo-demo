class Solution:
    def largestSquareArea(self, a, b):
        def intersecting_square_area(c, d, e, f):
            def maximum(x, y):
                return y if y > x else x

            def minimum(x, y):
                return y if y < x else x

            g = maximum(c[0], e[0])
            h = minimum(d[0], f[0])
            i = maximum(c[1], e[1])
            j = minimum(d[1], f[1])

            if g >= h:
                return 0
            if i >= j:
                return 0

            k = h - g
            l = j - i
            m = minimum(k, l)
            return m * m

        p = 0
        q = len(a)

        def loop_outer(r):
            if r > q - 2:
                return 1

            def loop_inner(s):
                nonlocal p
                if s > q - 1:
                    return 1
                t = intersecting_square_area(a[r], b[r], a[s], b[s])
                if t > p:
                    p = t
                return loop_inner(s + 1)

            loop_inner(r + 1)
            return loop_outer(r + 1)

        loop_outer(0)
        return p