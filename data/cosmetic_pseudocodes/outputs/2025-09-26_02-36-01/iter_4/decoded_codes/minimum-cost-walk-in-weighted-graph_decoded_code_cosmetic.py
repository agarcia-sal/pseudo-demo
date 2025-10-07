class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, u):
        p_arr = self.parent
        if p_arr[u] != u:
            p_arr[u] = self.find(p_arr[u])
        return p_arr[u]

    def union(self, u, v):
        root_of_u = self.find(u)
        root_of_v = self.find(v)
        if root_of_u != root_of_v:
            rank_arr = self.rank
            parent_arr = self.parent
            if not (rank_arr[root_of_u] <= rank_arr[root_of_v]):
                parent_arr[root_of_v] = root_of_u
            else:
                if rank_arr[root_of_u] < rank_arr[root_of_v]:
                    parent_arr[root_of_u] = root_of_v
                else:
                    parent_arr[root_of_v] = root_of_u
                    rank_arr[root_of_u] += 1


class Solution:
    def minimumCost(self, n, edges, query):
        uf = UnionFind(n)
        MAX_BITWISE_AND = (1 << 32) - 1
        cmp_and_list = [MAX_BITWISE_AND] * n

        for u, v, w in edges:
            uf.union(u, v)
            root_idx = uf.find(u)
            cmp_and_list[root_idx] &= w

        comp_cost_map = {}
        for i in range(n):
            current_root = uf.find(i)
            if current_root not in comp_cost_map:
                comp_cost_map[current_root] = cmp_and_list[current_root]

        res_list = []
        for start_node, end_node in query:
            if start_node == end_node:
                res_list.append(0)
            else:
                root_s = uf.find(start_node)
                root_t = uf.find(end_node)
                if root_s == root_t:
                    res_list.append(comp_cost_map[root_s])
                else:
                    res_list.append(-1)

        return res_list