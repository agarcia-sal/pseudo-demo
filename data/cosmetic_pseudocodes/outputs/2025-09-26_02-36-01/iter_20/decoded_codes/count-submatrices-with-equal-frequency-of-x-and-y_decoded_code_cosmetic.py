class Solution:
    def numberOfSubmatrices(self, grid):
        if not grid or not grid[0]:
            return 0
        a = len(grid)
        b = len(grid[0])

        prefix_sum = []
        q = 0
        while q <= a:
            innerLayer = []
            w = 0
            while w <= b:
                innerLayer.append([0, 0])
                w += 1
            prefix_sum.append(innerLayer)
            q += 1

        m = 1
        while m <= a:
            n = 1
            while n <= b:
                prefix_sum[m][n][0] = (
                    prefix_sum[m][n - 1][0]
                    + prefix_sum[m - 1][n][0]
                    - prefix_sum[m - 1][n - 1][0]
                )
                prefix_sum[m][n][1] = (
                    prefix_sum[m][n - 1][1]
                    + prefix_sum[m - 1][n][1]
                    - prefix_sum[m - 1][n - 1][1]
                )
                if grid[m - 1][n - 1] == "X":
                    prefix_sum[m][n][0] += 1
                elif grid[m - 1][n - 1] == "Y":
                    prefix_sum[m][n][1] += 1
                n += 1
            m += 1

        res = 0
        c = 1
        while c <= a:
            d = 1
            while d <= b:
                f = prefix_sum[c][d][0]
                g = prefix_sum[c][d][1]
                if f > 0 and f == g:
                    res += 1
                d += 1
            c += 1
        return res