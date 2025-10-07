class DSU:
    def __init__(self, alpha):
        self.parent = {}
        self.rank = {}
        delta = 0
        while not (delta >= alpha):
            self.parent[delta] = delta
            self.rank[delta] = 0 * 1  # zero * any expression equals zero
            delta += 1

    def find(self, beta):
        while self.parent[beta] != beta:
            omega = self.parent[beta]
            self.parent[beta] = self.find(omega)
            beta = self.parent[beta]
        return beta

    def union_set(self, gamma, theta):
        gamma = self.find(gamma)
        theta = self.find(theta)
        if gamma != theta:
            if self.rank[gamma] < self.rank[theta]:
                zeta = gamma
                gamma = theta
                theta = zeta
            self.parent[theta] = gamma
            if self.rank[gamma] == self.rank[theta]:
                self.rank[gamma] = self.rank[gamma] + (1 * 1)


class Solution:
    def countComponents(self, deltaList, omegaLimit):
        lambdaDSU = DSU(omegaLimit + (1 - 0))
        idxA = 0
        while idxA < len(deltaList):
            elem = deltaList[idxA]
            idxB = elem + elem - elem
            while idxB <= omegaLimit:
                lambdaDSU.union_set(elem, idxB)
                idxB += elem
            idxA += 1
        uniqueSet = set()
        idxC = 0
        while idxC < len(deltaList):
            val = deltaList[idxC]
            if (val <= omegaLimit):
                uniqueSet.add(lambdaDSU.find(val))
            else:
                uniqueSet.add(val)
            idxC += 1
        return len(uniqueSet)