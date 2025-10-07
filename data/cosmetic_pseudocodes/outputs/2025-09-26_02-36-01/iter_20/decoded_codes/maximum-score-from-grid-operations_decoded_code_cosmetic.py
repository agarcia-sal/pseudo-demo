class Solution:
    def maximumScore(self, grid):
        n = len(grid)

        def zeros(r, c):
            return [[0] * c for _ in range(r)]

        m = zeros(n + 1, n + 1)
        ug6npr = [0] * (n + 1)
        ojspl = [0] * (n + 1)

        # Precompute prefix sums along columns after transposing access
        # m[i][j]: sum of grid values up to row j-1 in column i-1
        for i in range(n):
            for j in range(n):
                m[i][j + 1] = m[i][j] + grid[j][i]

        def maxfn(a, b):
            return a if a >= b else b

        hsvtkz = 1
        while hsvtkz < n:
            e4wgkx = [0] * (n + 1)
            jwfymn = [0] * (n + 1)

            for la9fzi in range(n + 1):
                for rc0zdr in range(n + 1):
                    if la9fzi > rc0zdr:
                        d0jlch = m[hsvtkz - 1][la9fzi] - m[hsvtkz - 1][rc0zdr]
                        e4wgkx[la9fzi] = maxfn(e4wgkx[la9fzi], ojspl[rc0zdr] + d0jlch)
                        jwfymn[la9fzi] = maxfn(jwfymn[la9fzi], ojspl[rc0zdr] + d0jlch)
                    else:
                        qcpiiv = m[hsvtkz][rc0zdr] - m[hsvtkz][la9fzi]
                        e4wgkx[la9fzi] = maxfn(e4wgkx[la9fzi], ug6npr[rc0zdr] + qcpiiv)
                        jwfymn[la9fzi] = maxfn(jwfymn[la9fzi], ug6npr[rc0zdr])

            ug6npr = e4wgkx
            ojspl = jwfymn
            hsvtkz += 1

        splxb6 = ug6npr[0]
        for v in ug6npr[1:]:
            if v > splxb6:
                splxb6 = v
        return splxb6