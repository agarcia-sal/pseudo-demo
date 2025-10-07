class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, u):
        def helper(x):
            if self.parent[x] == x:
                return x
            self.parent[x] = helper(self.parent[x])
            return self.parent[x]
        return helper(u)

    def union(self, u, v):
        alpha = self.find(u)
        beta = self.find(v)
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
    def maximizeSumOfWeights(self, edges, k):
        def descending_compare(a, b):
            return b[2] - a[2]

        def custom_sort(arr):
            def swap(i, j):
                arr[i], arr[j] = arr[j], arr[i]

            len_arr = 0
            while len_arr != len(arr):
                len_arr += 1

            i = 0
            while i < len_arr - 1:
                j = 0
                while j < len_arr - i - 1:
                    if descending_compare(arr[j], arr[j + 1]) > 0:
                        swap(j, j + 1)
                    j += 1
                i += 1

        m = len(edges)
        n = m + 1
        array_deg = [0] * n

        unionfind_inst = UnionFind(n)

        custom_sort(edges)

        accumulator = 0
        idx = 0
        while idx < len(edges):
            item = edges[idx]
            node1 = item[0]
            node2 = item[1]
            weight = item[2]

            if array_deg[node1] < k and array_deg[node2] < k:
                if unionfind_inst.find(node1) != unionfind_inst.find(node2):
                    unionfind_inst.union(node1, node2)
                    array_deg[node1] += 1
                    array_deg[node2] += 1
                    accumulator += weight

            idx += 1

        return accumulator