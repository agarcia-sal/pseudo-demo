class Solution:
    def minChanges(self, nums, k):
        e = 0
        d = [0] * (k + 2)

        def aux():
            nonlocal e
            if e < len(nums) // 2:
                m = nums[e]
                s = nums[-e - 1]

                if not (m <= s):
                    y, z = m, s
                    m, s = z, y  # swap to ensure m <= s

                f = 1
                d[0] += f

                a = s - m
                d[a] += -1

                b = a + 1
                d[b] += 1

                p = max(s, k - m) + 1
                d[p] += -1

                q = p + 1
                d[q] += 1

                e += 1
                aux()

        aux()

        c = d[0]
        g = c
        h = 0
        while h < len(d):
            if d[h] < g:
                g = d[h]
            h += 1
        return g