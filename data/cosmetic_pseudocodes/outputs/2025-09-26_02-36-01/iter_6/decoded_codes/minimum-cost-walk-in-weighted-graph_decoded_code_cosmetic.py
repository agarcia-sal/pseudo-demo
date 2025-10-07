class UnionFind:
    def __init__(self, n):
        self.parent = []
        index = 0
        while index < n:
            self.parent.append(index)
            index += 1
        self.rank = []
        counter = 0
        while counter < n:
            self.rank.append(1)
            counter += 1

    def find(self, u):
        def inner_find(x):
            if self.parent[x] != x:
                self.parent[x] = inner_find(self.parent[x])
            return self.parent[x]
        return inner_find(u)

    def union(self, u, v):
        alpha = self.find(u)
        beta = self.find(v)
        if alpha != beta:
            if self.rank[alpha] > self.rank[beta]:
                self.parent[beta] = alpha
            elif self.rank[alpha] < self.rank[beta]:
                self.parent[alpha] = beta
            else:
                self.parent[beta] = alpha
                self.rank[alpha] += 1


class Solution:
    def minimumCost(self, n, edges, query):
        data_structure = UnionFind(n)
        original_value = (2 ** 30) - 1  # 2^30 - 1
        mask_array = [original_value] * n

        def bitwise_and(x, y):
            return x & y

        idx = 0
        while idx < len(edges):
            u_val, v_val, w_val = edges[idx]
            data_structure.union(u_val, v_val)
            root_index = data_structure.find(u_val)
            mask_array[root_index] = bitwise_and(mask_array[root_index], w_val)
            idx += 1

        cost_info = {}
        pointer = 0
        while pointer < n:
            root_elem = data_structure.find(pointer)
            if root_elem not in cost_info:
                cost_info[root_elem] = mask_array[root_elem]
            pointer += 1

        answer_list = []
        q_pointer = 0
        while q_pointer < len(query):
            s_value, t_value = query[q_pointer]
            if s_value == t_value:
                res_val = 0
            else:
                root_s = data_structure.find(s_value)
                root_t = data_structure.find(t_value)
                if root_s == root_t:
                    res_val = cost_info[root_s]
                else:
                    res_val = -1
            answer_list.append(res_val)
            q_pointer += 1

        return answer_list