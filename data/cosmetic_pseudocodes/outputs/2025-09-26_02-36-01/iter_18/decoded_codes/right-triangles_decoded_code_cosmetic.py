class Solution:
    def numberOfRightTriangles(self, grid):
        a = len(grid)
        b = len(grid[0])
        total_result = 0

        c = 0
        while c < a:
            d = 0
            while d < b:
                if grid[c][d] != 1:
                    d += 1
                    continue

                e = 0
                f = 0
                g = 0
                while g < b:
                    if g != d:
                        e += grid[c][g]
                    g += 1

                h = 0
                while h < a:
                    if h != c:
                        f += grid[h][d]
                    h += 1

                total_result += e * f
                d += 1
            c += 1

        return total_result