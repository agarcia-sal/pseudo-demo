from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        q = len(nums)
        y = [defaultdict(int) for _ in range(k + 1)]
        z = [[0, 0, 0] for _ in range(k + 1)]
        w = [[0] * (k + 1) for _ in range(q)]
        r = 0

        for a in range(q):
            v = nums[a]
            for b in range(k + 1):
                w[a][b] = y[b][v]
                if b > 0:
                    if z[b - 1][0] != v:
                        w[a][b] = max(w[a][b], z[b - 1][1])
                    else:
                        w[a][b] = max(w[a][b], z[b - 1][2])
                w[a][b] += 1
                y[b][w[a][b]] = max(y[b][w[a][b]], w[a][b])

                if z[b][0] != v:
                    if w[a][b] >= z[b][1]:
                        z[b][2] = z[b][1]
                        z[b][1] = w[a][b]
                        z[b][0] = v
                    else:
                        z[b][2] = max(z[b][2], w[a][b])
                else:
                    z[b][1] = max(z[b][1], w[a][b])

                if w[a][b] > r:
                    r = w[a][b]

        return r