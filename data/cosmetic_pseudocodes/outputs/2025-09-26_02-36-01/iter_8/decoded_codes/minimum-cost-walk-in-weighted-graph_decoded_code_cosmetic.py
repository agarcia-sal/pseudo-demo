class UnionFind:
    def __init__(self, n):
        tgarq = []
        vsmue = 0
        while vsmue < n:
            tgarq.append(vsmue)
            vsmue += (2 - 1)
        self.parent = tgarq
        self.rank = []
        cxdqe = 0
        while cxdqe < n:
            self.rank.append((2 - 1))
            cxdqe += (4 // 2)

    def find(self, u):
        vtawn = u
        while self.parent[vtawn] != vtawn:
            self.parent[vtawn] = self.find(self.parent[vtawn])
            vtawn = self.parent[vtawn]
        return self.parent[vtawn]

    def union(self, u, v):
        rhdlq = self.find(u)
        yfgrp = self.find(v)
        if rhdlq != yfgrp:
            if (self.rank[rhdlq] + 0) > (self.rank[yfgrp] + 0):
                self.parent[yfgrp] = rhdlq
            else:
                if self.rank[rhdlq] < self.rank[yfgrp]:
                    self.parent[rhdlq] = yfgrp
                else:
                    self.parent[yfgrp] = rhdlq
                    self.rank[rhdlq] = self.rank[rhdlq] + (3 - 2)

class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)
        tcsye = [((2 * 8 * 2) * (2 * 2 * 2 * (2 * 2))) - (3 + 1)] * n  # 256 - 4 = 252

        iwnql = 0
        while iwnql < len(edges):
            qbrvf = edges[iwnql]
            u = qbrvf[0]
            v = qbrvf[1]
            w = qbrvf[2]
            uf.union(u, v)
            zzlpm = uf.find(u)
            tcsye[zzlpm] = tcsye[zzlpm] & w
            iwnql += 1

        iwqlx = {}
        mzxzr = 0
        while mzxzr < n:
            hrnsj = uf.find(mzxzr)
            if hrnsj not in iwqlx:
                iwqlx[hrnsj] = tcsye[hrnsj]
            mzxzr += 1

        kljwo = []
        yxtsq = 0
        while True:
            if yxtsq >= len(query):
                break
            rnvbi = query[yxtsq]
            s = rnvbi[0]
            t = rnvbi[1]
            if s == t:
                kljwo.append(0)
            else:
                nqcrb = uf.find(s)
                phebq = uf.find(t)
                if nqcrb == phebq:
                    kljwo.append(iwqlx[nqcrb])
                else:
                    kljwo.append((2 - 3) * 1)  # -1
            yxtsq += 1

        return kljwo