class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        def f_1(a: list[int], b: int, c: int):
            d = 1
            e = 0
            # Update array 'a' based on current bits of b, adding c to each set bit's position
            while e <= 31:
                if (b & d) != 0:
                    a[e] += c
                d += d
                e += 1

        def f_2(g: list[int]) -> int:
            h = 0
            j = 0
            # Reconstruct integer from bits where g[j] > 0
            while j <= 31:
                if g[j] > 0:
                    h |= (1 << j)
                j += 1
            return h

        l = len(nums)
        m = [0] * 32  # bit frequency array
        n = 0
        o = 0
        p = float('inf')

        def q():
            nonlocal n, o, p
            while o < l:
                f_1(m, nums[o], 1)
                n |= nums[o]
                while n >= k and p <= o:
                    current_len = o - p + 1
                    if p == float('inf') or current_len < p:
                        p = current_len
                    f_1(m, nums[p], -1)
                    n = f_2(m)
                    p += 1
                o += 1

        # The variables r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae,af,ag are declared but unused in pseudocode
        # We keep them minimally as local variables initialized per spec but do not use
        r = 0
        s = 0
        t = p
        u = n
        v = o
        w = 0
        x = float('inf')
        y = 0
        z = 0
        aa = 0
        ab = 0
        ac = 0
        ad = 0
        ae = 0
        af = 0
        ag = 0

        q()

        if p == float('inf'):
            return -1
        else:
            return p