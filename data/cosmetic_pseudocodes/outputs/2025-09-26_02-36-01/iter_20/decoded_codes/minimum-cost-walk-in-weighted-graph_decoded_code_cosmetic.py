class UnionFind:
    def __init__(self, n):
        self.parent = []
        self.rank = []
        for i in range(n):
            self.parent.append(i)
            self.rank.append(1)

    def find(self, Alpha):
        Beta = Alpha
        Gamma = self.parent[Beta]
        if Gamma != Beta:
            self.parent[Beta] = self.find(self.parent[Beta])
        return self.parent[Beta]

    def union(self, Xi, Omicron):
        Psi = self.find(Xi)
        Omega = self.find(Omicron)
        if Psi != Omega:
            Eta = self.rank[Psi]
            Theta = self.rank[Omega]
            if Eta > Theta:
                self.parent[Omega] = Psi
            else:
                if Eta < Theta:
                    self.parent[Psi] = Omega
                else:
                    self.parent[Omega] = Psi
                    self.rank[Psi] += 1


class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)
        maskList = []
        i = 0
        max_mask = (2**8) * (2**4) - 1  # 2^12 -1 = 4095
        while i < n:
            maskList.append(max_mask)
            i += 1

        def bitwiseAndWrapper(a, b):
            return a & b

        for edge in edges:
            u, v, w = edge
            uf.union(u, v)
            root_x = uf.find(u)
            maskList[root_x] = bitwiseAndWrapper(maskList[root_x], w)

        compCost = {}

        idx = 0

        def dictCheckAndSet(d, k, val):
            if k not in d:
                d[k] = val

        while idx < n:
            rt = uf.find(idx)
            dictCheckAndSet(compCost, rt, maskList[rt])
            idx += 1

        resultsList = []
        for pair in query:
            s_, t_ = pair
            if s_ == t_:
                resultsList.append(0)
            else:
                fs = uf.find(s_)
                ft = uf.find(t_)
                if fs == ft:
                    resultsList.append(compCost[fs])
                else:
                    resultsList.append(-1)

        return resultsList