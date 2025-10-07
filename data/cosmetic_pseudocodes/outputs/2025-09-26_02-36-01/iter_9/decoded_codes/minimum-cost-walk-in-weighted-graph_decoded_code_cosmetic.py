class UnionFind:
    def __init__(self, m):
        self.parent = [i for i in range(m)]
        self.rank = [1] * m

    def find(self, x):
        def helper(y):
            if self.parent[y] == y:
                return y
            self.parent[y] = helper(self.parent[y])
            return self.parent[y]
        return helper(x)

    def union(self, r, s):
        rootA = self.find(r)
        rootB = self.find(s)
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                self.rank[rootA] += 1


class Solution:
    def minimumCost(self, p, edges, queries):
        uf = UnionFind(p)
        full_mask = (1 << 32) - 1
        bitwise_accumulator = [full_mask] * p

        def process_edges(lst):
            idx = 0

            def reduce_edge():
                nonlocal idx
                if idx >= len(lst):
                    return
                a, b, c = lst[idx]
                uf.union(a, b)
                par = uf.find(a)
                bitwise_accumulator[par] &= c
                idx += 1
                reduce_edge()

            reduce_edge()

        process_edges(edges)

        components_map = {}
        for j in range(p):
            leader = uf.find(j)
            if leader not in components_map:
                components_map[leader] = bitwise_accumulator[leader]

        output = []

        def query_handler(lst2):
            k = 0
            while k < len(lst2):
                first_val, second_val = lst2[k]
                if first_val == second_val:
                    output.append(0)
                else:
                    first_leader = uf.find(first_val)
                    second_leader = uf.find(second_val)
                    if first_leader == second_leader:
                        output.append(components_map[first_leader])
                    else:
                        output.append(-1)
                k += 1

        query_handler(queries)

        return output