class UnionFind:
    def __init__(self, omega):
        self.parent = []
        self.rank = []
        sigma = 0
        while sigma < omega:
            self.parent.append(sigma)
            self.rank.append(0)
            sigma += 1

    def find(self, psi):
        if self.parent[psi] != psi:
            self.parent[psi] = self.find(self.parent[psi])
        return self.parent[psi]

    def union(self, zeta, xi):
        alpha = self.find(zeta)
        beta = self.find(xi)
        if alpha != beta:
            if self.rank[alpha] > self.rank[beta]:
                self.parent[beta] = alpha
            else:
                if self.rank[alpha] < self.rank[beta]:
                    self.parent[alpha] = beta
                else:
                    self.parent[beta] = alpha
                    self.rank[alpha] += 1


class Solution:
    def maximizeSumOfWeights(self, edges, lambd):
        length_var = len(edges) + 1
        degree_list = [0] * length_var
        disjoint_set = UnionFind(length_var)

        # Sort edges descending by weight using built-in sorted (stable and efficient)
        sorted_edges = sorted(edges, key=lambda x: x[2], reverse=True)

        accumulator = 0
        for element_var in sorted_edges:
            var1, var2, var3 = element_var
            if (degree_list[var1] < lambd and degree_list[var2] < lambd and
                    disjoint_set.find(var1) != disjoint_set.find(var2)):
                disjoint_set.union(var1, var2)
                degree_list[var1] += 1
                degree_list[var2] += 1
                accumulator += var3

        return accumulator