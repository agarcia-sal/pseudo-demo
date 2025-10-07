from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        m = len(nums)
        q = [[0] * (k + 1) for _ in range(m)]
        s = [defaultdict(int) for _ in range(k + 1)]
        t = [[0, 0, 0] for _ in range(k + 1)]

        for l in range(m):
            v = nums[l]
            for u in range(k + 1):
                q[l][u] = s[u].get(v, 0)
                if u > 0:
                    if t[u-1][0] != v:
                        w = t[u-1][1]
                        if w > q[l][u]:
                            q[l][u] = w
                    else:
                        w = t[u-1][2]
                        if w > q[l][u]:
                            q[l][u] = w
                q[l][u] += 1
                s[u][v] = max(s[u].get(v, 0), q[l][u])

                if t[u][0] != v:
                    if q[l][u] >= t[u][1]:
                        t[u][2] = t[u][1]
                        t[u][1] = q[l][u]
                        t[u][0] = v
                    else:
                        if q[l][u] > t[u][2]:
                            t[u][2] = q[l][u]
                else:
                    if q[l][u] > t[u][1]:
                        t[u][1] = q[l][u]

        p = 0
        for x in range(m):
            for y in range(k + 1):
                if q[x][y] > p:
                    p = q[x][y]
        return p