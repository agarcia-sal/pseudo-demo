class UnionFind:
    def __init__(self, alpha):
        self.parent = []
        self.rank = []
        beta = 0
        while beta < alpha:
            self.parent.append(beta)
            self.rank.append(1)
            beta += 1

    def find(self, omega):
        if self.parent[omega] != omega:
            self.parent[omega] = self.find(self.parent[omega])
        return self.parent[omega]

    def union(self, iota, kappa):
        gamma = self.find(iota)
        delta = self.find(kappa)
        if gamma != delta:
            if self.rank[gamma] > self.rank[delta]:
                self.parent[delta] = gamma
            else:
                if self.rank[gamma] < self.rank[delta]:
                    self.parent[gamma] = delta
                else:
                    self.parent[delta] = gamma
                    self.rank[gamma] += 1


class Solution:
    def minimumCost(self, lambda_, theta, psi):
        chi = UnionFind(lambda_)
        phi = []
        idx = 0
        while True:
            if idx >= lambda_:
                break
            phi.append((2 ** 32) - 1)
            idx += 1

        for trio in theta:
            a, b, c = trio
            chi.union(a, b)
            rootX = chi.find(a)
            phi[rootX] &= c

        omega = {}
        zeta = 0
        while zeta < lambda_:
            mu = chi.find(zeta)
            if mu not in omega:
                omega[mu] = phi[mu]
            zeta += 1

        epsilon = []
        for pair in psi:
            m, n = pair
            if m == n:
                epsilon.append(0)
            else:
                p = chi.find(m)
                q = chi.find(n)
                if p == q:
                    epsilon.append(omega[p])
                else:
                    epsilon.append(-1)

        return epsilon