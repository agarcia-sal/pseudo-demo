class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        D = 1 << 7
        L = len(nums)
        # f[l+1][k+2][D] boolean DP table
        f = [[[False] * D for _ in range(k + 2)] for __ in range(L + 1)]
        f[0][0][0] = True

        def updateF(a: int, b: int, c: int, d: int) -> None:
            # Propagate states without selecting new element
            f[a][b][c] = f[a][b][c] or f[d][b][c]

        def updateFBitwise(a: int, b: int, c: int, d: int, e: int) -> None:
            # Propagate states selecting new element, combine bitmasks
            tempBit = c | e
            if 0 <= b < len(f[0]):
                f[a][b][tempBit] = True

        def forward() -> None:
            p = 0
            while p < L:
                q = 0
                while q <= k:
                    r = 0
                    while r < D:
                        if f[p][q][r]:
                            updateF(p + 1, q, r, p)
                            if q + 1 <= k:
                                updateFBitwise(p + 1, q + 1, r, p, nums[p])
                        r += 1
                    q += 1
                p += 1

        forward()

        g = [[[False] * D for _ in range(k + 2)] for __ in range(L + 1)]
        g[L][0][0] = True

        def updateG(a: int, b: int, c: int, d: int) -> None:
            g[a][b][c] = g[a][b][c] or g[d][b][c]

        def updateGBitwise(a: int, b: int, c: int, d: int, e: int) -> None:
            tempBit = c | e
            if 0 <= b < len(g[0]):
                g[a][b][tempBit] = True

        def backward() -> None:
            u = L
            while u > 0:
                v = 0
                while v <= k:
                    w = 0
                    while w < D:
                        if g[u][v][w]:
                            updateG(u - 1, v, w, u)
                            if v + 1 <= k:
                                updateGBitwise(u - 1, v + 1, w, u, nums[u - 1])
                        w += 1
                    v += 1
                u -= 1

        backward()

        ans = 0

        def BoolIsTrue(flag: bool) -> bool:
            return flag is True

        idx = k
        while idx <= L - k:
            bitX = 0
            while bitX < D:
                if BoolIsTrue(f[idx][k][bitX]):
                    bitY = 0
                    while bitY < D:
                        if BoolIsTrue(g[idx][k][bitY]):
                            candidate = bitX ^ bitY
                            if candidate > ans:
                                ans = candidate
                        bitY += 1
                bitX += 1
            idx += 1

        return ans