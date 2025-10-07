class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(x: int, y: int) -> int:
            # ((x & 1) ^ y) == 1 means if the parity of x and y differs
            if ((x & 1) ^ y) == 1:
                return x + 1
            else:
                return x + 2

        u = len(nums1)
        v = len(nums2)
        # q is a (u+1) x (v+1) matrix initialized with 0
        q = [[0] * (v + 1) for _ in range(u + 1)]

        # Using 1-based indexing logic as in pseudocode,
        # but adapting Python 0-based indexing by offsetting indices with -1 carefully
        # Note: pseudocode accesses nums1 and nums2 from index 1,
        # so nums1[a] in pseudocode corresponds to nums1[a-1] in Python.

        a = 1
        while a <= u:
            p = nums1[a - 1]
            q[a][0] = nxt(q[a - 1][0], p)
            a += 1

        b = 1
        while b <= v:
            r = nums2[b - 1]
            q[0][b] = nxt(q[0][b - 1], r)
            b += 1

        c = 1
        while c <= u:
            s = nums1[c - 1]
            d = 1
            while d <= v:
                t = nums2[d - 1]
                val1 = nxt(q[c - 1][d], s)
                val2 = nxt(q[c][d - 1], t)
                q[c][d] = val1 if val1 < val2 else val2
                d += 1
            c += 1

        return q[u][v]