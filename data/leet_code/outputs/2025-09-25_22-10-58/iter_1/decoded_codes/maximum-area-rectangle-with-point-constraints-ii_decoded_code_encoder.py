from bisect import bisect_left
from itertools import pairwise

class Fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

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
        points = sorted(zip(xCoord, yCoord))
        ys = sorted(set(yCoord))
        ans = -1
        tree = Fenwick(len(ys))
        # Add the first point's y index
        tree.add(bisect_left(ys, points[0][1]) + 1)
        pre = {}

        for (x1, y1), (x2, y2) in pairwise(points):
            y = bisect_left(ys, y2) + 1
            tree.add(y)
            if x1 != x2:
                continue
            cur = tree.query(bisect_left(ys, y1) + 1, y)
            if y2 in pre and pre[y2][1] == y1 and pre[y2][2] + 2 == cur:
                ans = max(ans, (x2 - pre[y2][0]) * (y2 - y1))
            pre[y2] = (x1, y1, cur)

        return ans