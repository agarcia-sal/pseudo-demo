class Solution:
    def maxScore(self, grid):
        u_1 = len(grid)
        u_2 = len(grid[0])
        h_p = [[float('inf')] * u_2 for _ in range(u_1)]
        h_p[0][0] = grid[0][0]
        v_c = -float('inf')

        idx_q = 1
        while idx_q < u_2:
            if h_p[0][idx_q - 1] < grid[0][idx_q]:
                h_p[0][idx_q] = h_p[0][idx_q - 1]
            else:
                h_p[0][idx_q] = grid[0][idx_q]
            idx_q += 1

        idx_p = 1
        while idx_p < u_1:
            if h_p[idx_p - 1][0] < grid[idx_p][0]:
                h_p[idx_p][0] = h_p[idx_p - 1][0]
            else:
                h_p[idx_p][0] = grid[idx_p][0]
            idx_p += 1

        _x = 1
        while _x < u_1:
            _y = 1
            while _y < u_2:
                if h_p[_x][_y - 1] < h_p[_x - 1][_y]:
                    h_p[_x][_y] = h_p[_x][_y - 1]
                else:
                    h_p[_x][_y] = h_p[_x - 1][_y]

                g_m = grid[_x][_y] - h_p[_x][_y]
                if g_m > v_c:
                    v_c = g_m
                _y += 1
            _x += 1

        return v_c