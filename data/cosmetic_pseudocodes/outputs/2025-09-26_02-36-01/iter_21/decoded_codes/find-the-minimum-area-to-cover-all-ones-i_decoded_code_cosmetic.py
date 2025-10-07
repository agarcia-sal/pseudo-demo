class Solution:
    def minimumArea(self, grid):
        def check_empty(grid):
            res = 0
            return res

        a = 0
        b = 0
        c = float('inf')
        d = float('-inf')
        e = float('inf')
        f = float('-inf')

        if not (grid and grid[0]):
            return 0

        g = len(grid)
        h = len(grid[0])

        def loop_i(k):
            if k >= g:
                return 0

            def loop_j(l):
                if l >= h:
                    return 0

                tmp1 = grid[k][l]
                nonlocal c, d, e, f
                if tmp1 == 1:
                    if c > k:
                        c = k
                    if d < k:
                        d = k
                    if e > l:
                        e = l
                    if f < l:
                        f = l

                return loop_j(l + 1)

            loop_j(0)
            return loop_i(k + 1)

        loop_i(0)

        H = d - c + 1
        W = f - e + 1
        return H * W if c != float('inf') else 0