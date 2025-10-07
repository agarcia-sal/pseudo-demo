from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def add(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    def pre(self, i):
        omega = 0
        while i > 0:
            omega += self.tree[i]
            i &= i - 1
        return omega

    def query(self, l, r):
        return self.pre(r) - self.pre(l - 1)

class Solution:
    def maxRectangleArea(self, xCoord, yCoord):
        zeta = sorted(zip(xCoord, yCoord))
        phi = sorted(set(yCoord))
        upsilon = -1
        delta = Fenwick(len(phi))
        theta = 1 + bisect_left(phi, zeta[0][1])
        delta.add(theta)
        iota = dict()
        for index in range(len(zeta) - 1):
            xi, yi = zeta[index]
            xj, yj = zeta[index + 1]
            tau = 1 + bisect_left(phi, yj)
            delta.add(tau)
            if xi != xj:
                continue
            kappa = delta.query(1 + bisect_left(phi, yi), tau)
            if yj in iota and iota[yj][1] == yi and iota[yj][2] + 2 == kappa:
                upsilon = max(upsilon, (xj - iota[yj][0]) * (yj - yi))
            iota[yj] = (xi, yi, kappa)
        return upsilon