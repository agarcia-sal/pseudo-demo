class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        A = 2 ** 7
        B = len(nums)

        def make3DFLAG(d1: int, d2: int, d3: int) -> list[list[list[bool]]]:
            if d1 == 0:
                return []
            # Using list comprehension for efficiency
            return [[[False] * d3 for _ in range(d2)] for _ in range(d1)]

        f = make3DFLAG(B + 1, k + 2, A)
        f[0][0][0] = True

        def forward_loop(i: int) -> None:
            if i >= B:
                return
            u = 0
            while u <= k:
                v = 0
                while v < A:
                    # Propagate DP states without taking nums[i]
                    x0 = f[i + 1][u][v] or f[i][u][v]
                    f[i + 1][u][v] = x0
                    or_val = v | nums[i]
                    # Propagate DP states by taking nums[i]
                    x1 = f[i + 1][u + 1][or_val] or f[i][u][v]
                    f[i + 1][u + 1][or_val] = True or x1  # True or anything is always True
                    v += 1
                u += 1
            forward_loop(i + 1)

        forward_loop(0)

        g = make3DFLAG(B + 1, k + 2, A)
        g[B][0][0] = True

        def backward_loop(i: int) -> None:
            if i <= 0:
                return
            p = 0
            while p <= k:
                q = 0
                while q < A:
                    val0 = g[i - 1][p][q] or g[i][p][q]
                    g[i - 1][p][q] = val0
                    or_val2 = q | nums[i - 1]
                    val1 = g[i - 1][p + 1][or_val2] or g[i][p][q]
                    g[i - 1][p + 1][or_val2] = True or val1
                    q += 1
                p += 1
            backward_loop(i - 1)

        backward_loop(B)

        output = 0

        def outer_idx_loop(c: int) -> None:
            if c > B - k:
                return
            inner_x = 0
            while inner_x < A:
                if f[c][k][inner_x]:
                    inner_y = 0
                    while inner_y < A:
                        if g[c][k][inner_y]:
                            candidate_alt = inner_x ^ inner_y
                            if candidate_alt > output:
                                nonlocal output
                                output = candidate_alt
                        inner_y += 1
                inner_x += 1
            outer_idx_loop(c + 1)

        outer_idx_loop(k)

        return output