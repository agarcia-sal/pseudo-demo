from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        u = len(image)
        v = len(image[0]) if u > 0 else 0
        alpha = [[0] * v for _ in range(u)]
        beta = [[0] * v for _ in range(u)]

        neighborhood = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def checkRegion(p: int, q: int) -> bool:
            def recursive_i(r: int, s: int) -> bool:
                if r == p + 3:
                    return True

                def recursive_j(t: int) -> bool:
                    if t == q + 3:
                        return recursive_i(r + 1, s)

                    rr = r
                    ss = t

                    def recursive_dx_dy(index: int) -> bool:
                        if index == len(neighborhood):
                            return recursive_j(t + 1)

                        offX, offY = neighborhood[index]
                        nx = rr + offX
                        ny = ss + offY
                        if p <= nx < p + 3 and q <= ny < q + 3:
                            if abs(image[rr][ss] - image[nx][ny]) > threshold:
                                return False
                        return recursive_dx_dy(index + 1)

                    return recursive_dx_dy(0)

                return recursive_j(s)

            return recursive_i(p, q)

        def avgValue(x: int, y: int) -> int:
            acc = 0
            for i_inner in range(x, x + 3):
                for j_inner in range(y, y + 3):
                    acc += image[i_inner][j_inner]
            return acc // 9

        outer_i = 0
        while outer_i < u - 2:
            outer_j = 0
            while outer_j < v - 2:
                if checkRegion(outer_i, outer_j):
                    avg_r = avgValue(outer_i, outer_j)
                    xx = outer_i
                    while xx < outer_i + 3:
                        yy = outer_j
                        while yy < outer_j + 3:
                            alpha[xx][yy] += avg_r
                            beta[xx][yy] += 1
                            yy += 1
                        xx += 1
                outer_j += 1
            outer_i += 1

        final_i = 0
        while final_i < u:
            final_j = 0
            while final_j < v:
                if beta[final_i][final_j] > 0:
                    new_val = alpha[final_i][final_j] // beta[final_i][final_j]
                    alpha[final_i][final_j] = new_val
                else:
                    alpha[final_i][final_j] = image[final_i][final_j]
                final_j += 1
            final_i += 1

        return alpha