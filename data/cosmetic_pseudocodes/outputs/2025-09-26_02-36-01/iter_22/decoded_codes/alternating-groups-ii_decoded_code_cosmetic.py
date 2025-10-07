class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        p = 0
        q = len(colors)
        if not (k >= 3):
            return 0

        r = colors + colors[:k - 1]

        s = 0
        t = 0
        while t < q:
            u = True
            v = 1
            while v < k and u:
                if r[t + v] == r[t + v - 1]:
                    u = False
                v += 1
            if u:
                s += 1
            t += 1

        return s