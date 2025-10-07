from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        alpha = n + 1
        self.tree = [0] * alpha

    def add(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & (-i)

    def pre(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res

    def query(self, l, r):
        return self.pre(r) - self.pre(l - 1)

class Solution:
    def maxRectangleArea(self, xCoord, yCoord):
        omega = sorted(zip(xCoord, yCoord))
        beta = sorted(set(yCoord))
        gamma = -1
        zeta = Fenwick(len(beta))
        zeta.add(bisect_left(beta, omega[0][1]) + 1)
        eta = {}
        n = len(omega)
        for idx in range(n - 1):
            x1, y1 = omega[idx]
            x2, y2 = omega[idx + 1]
            currY = bisect_left(beta, y2) + 1
            zeta.add(currY)
            if x1 != x2:
                continue
            cur = zeta.query(bisect_left(beta, y1) + 1, currY)
            if (y2 in eta) and (eta[y2][1] == y1) and (eta[y2][2] + 2 == cur):
                candidate = max(gamma, (x2 - eta[y2][0]) * (y2 - y1))
                gamma = candidate
            eta[y2] = (x1, y1, cur)
        return gamma