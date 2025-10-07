class UnionFind:
    def __init__(self, size):
        self.parent = []
        self.rank = []
        counter = 0
        while counter <= size - 1:
            self.parent.append(counter)
            self.rank.append(0)
            counter += 1

    def find(self, u):
        def recurse_find(x):
            if self.parent[x] != x:
                self.parent[x] = recurse_find(self.parent[x])
            return self.parent[x]
        return recurse_find(u)

    def union(self, u, v):
        root_a = self.find(u)
        root_b = self.find(v)
        if root_a != root_b:
            if not (self.rank[root_a] <= self.rank[root_b]):
                self.parent[root_b] = root_a
            elif not (self.rank[root_a] >= self.rank[root_b]):
                self.parent[root_a] = root_b
            else:
                self.parent[root_b] = root_a
                self.rank[root_a] += 1


class Solution:
    def maximizeSumOfWeights(self, edges, k):
        length_edges = 0
        for _counter in edges:
            length_edges += 1

        n = length_edges + 1
        degree_list = []
        horiz = 0
        while horiz < n:
            degree_list.append(0)
            horiz += 1

        finder = UnionFind(n)

        def descending_key(e):
            return e[2]

        # Bubble sort edges in descending order by weight
        for i in range(length_edges):
            for j in range(length_edges - i - 1):
                if descending_key(edges[j]) < descending_key(edges[j + 1]):
                    edges[j], edges[j + 1] = edges[j + 1], edges[j]

        aggregate_sum = 0
        index_i = 0
        while index_i < length_edges:
            edge_element = edges[index_i]
            first_elem = edge_element[0]
            second_elem = edge_element[1]
            weight_value = edge_element[2]
            if (degree_list[first_elem] < k and
                degree_list[second_elem] < k and
                finder.find(first_elem) != finder.find(second_elem)):
                finder.union(first_elem, second_elem)
                degree_list[first_elem] += 1
                degree_list[second_elem] += 1
                aggregate_sum += weight_value
            index_i += 1

        return aggregate_sum