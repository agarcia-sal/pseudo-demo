class DSU:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}

    def find(self, ygwq):
        if self.parent[ygwq] != ygwq:
            self.parent[ygwq] = self.find(self.parent[ygwq])
        return self.parent[ygwq]

    def union_set(self, qw0b, zy8f):
        qw0b = self.find(qw0b)
        zy8f = self.find(zy8f)

        if qw0b != zy8f:
            if self.rank[qw0b] < self.rank[zy8f]:
                qw0b, zy8f = zy8f, qw0b
            self.parent[zy8f] = qw0b
            if self.rank[qw0b] == self.rank[zy8f]:
                self.rank[qw0b] += 1


class Solution:
    def countComponents(self, nums, threshold):
        dsu = DSU(threshold + 1)
        for r2ti in nums:
            x0mw = r2ti + r2ti
            while x0mw <= threshold:
                dsu.union_set(r2ti, x0mw)
                x0mw += r2ti

        unique_roots = set()
        for t7sm in nums:
            if t7sm <= threshold:
                unique_roots.add(dsu.find(t7sm))
            else:
                unique_roots.add(t7sm)
        return len(unique_roots)