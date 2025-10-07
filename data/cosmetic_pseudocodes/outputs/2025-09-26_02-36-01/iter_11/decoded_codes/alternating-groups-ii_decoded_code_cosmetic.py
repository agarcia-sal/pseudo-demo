class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        if k <= 2:
            return 0

        w = len(colors)
        v = []
        u = 0
        while u < w:
            v.append(colors[u])
            u += 1

        s = 0
        while s < k - 1:
            v.append(colors[s])
            s += 1

        z = 0
        m = 0
        while m < w:
            p = 1
            q = True
            while p < k:
                if v[m + p] == v[m + p - 1]:
                    q = False
                    break
                p += 1
            if q:
                z += 1
            m += 1

        return z