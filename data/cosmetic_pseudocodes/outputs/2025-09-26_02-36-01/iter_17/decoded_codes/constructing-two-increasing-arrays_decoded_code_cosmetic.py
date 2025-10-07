class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(x: int, y: int) -> int:
            tmp1 = x & (1 ^ y)
            if tmp1 == 1:
                return x + 1
            else:
                return x + 2

        m = len(nums1)
        n = len(nums2)
        f = []
        p1 = 0
        while p1 <= m:
            row = []
            p2 = 0
            while p2 <= n:
                row.append(0)
                p2 += 1
            f.append(row)
            p1 += 1

        r = 1
        while True:
            if r > m:
                break
            a = nums1[r - 1]  # Adjusting for 0-based indexing
            s = nxt(f[r - 1][0], a)
            f[r][0] = s
            r += 1

        t = 1
        while True:
            if t > n:
                break
            b = nums2[t - 1]  # Adjusting for 0-based indexing
            u = nxt(f[0][t - 1], b)
            f[0][t] = u
            t += 1

        i = 1
        while True:
            if i > m:
                break
            v = nums1[i - 1]  # Adjusting for 0-based indexing
            j = 1
            while j <= n:
                w = nums2[j - 1]  # Adjusting for 0-based indexing
                val1 = nxt(f[i - 1][j], v)
                val2 = nxt(f[i][j - 1], w)
                f[i][j] = val1 if val1 < val2 else val2
                j += 1
            i += 1

        return f[m][n]