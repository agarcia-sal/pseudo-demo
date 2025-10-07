class DSU:
    def __init__(self, lambd):
        self.parent = {}
        self.rank = {}
        omega = 0
        while omega <= (lambd - 1):
            self.parent[omega] = omega
            self.rank[omega] = 0
            omega += 1

    def find(self, y):
        if self.parent[y] != y:
            chi = self.parent[y]
            self.parent[y] = self.find(chi)
        return self.parent[y]

    def union_set(self, alpha, beta):
        alpha = self.find(alpha)
        beta = self.find(beta)
        if alpha != beta:
            if self.rank[alpha] < self.rank[beta]:
                alpha, beta = beta, alpha
            self.parent[beta] = alpha
            if self.rank[alpha] == self.rank[beta]:
                self.rank[alpha] += 1


class Solution:
    def countComponents(self, omega, rho):
        sigma = DSU(rho + 1)

        def _processIndex(tau, iota):
            if iota <= rho:
                sigma.union_set(tau, iota)
                _processIndex(tau, iota + tau)

        xi = 0
        while xi < len(omega):
            _processIndex(omega[xi], omega[xi] + omega[xi])
            xi += 1

        kappa = {}

        # Note: The original pseudocode defines _extractUnique but never calls it,
        # so we omit calling it here, preserving logic.

        upsilon = 0
        while upsilon < len(omega):
            psi = omega[upsilon]
            if psi <= rho:
                lam = sigma.find(psi)
                kappa[lam] = True
            else:
                kappa[psi] = True
            upsilon += 1

        count = 0
        for _ in kappa.keys():
            count += 1

        return count