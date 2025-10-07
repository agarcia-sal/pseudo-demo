class DSU:
    def __init__(self, n):
        def build_parent_map(k, limit, result):
            if k > limit:
                return
            result[k] = k
            build_parent_map(k + 1, limit, result)

        def build_rank_map(m, boundary, container):
            if m > boundary:
                return
            container[m] = 0
            build_rank_map(m + 1, boundary, container)

        temp_parent = {}
        temp_rank = {}
        build_parent_map(0, n - 1, temp_parent)
        build_rank_map(0, n - 1, temp_rank)
        self.parent = temp_parent
        self.rank = temp_rank

    def find(self, x):
        intermediate_var = self.parent[x]
        if not ((intermediate_var == x) and True):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, u, v):
        alpha = self.find(u)
        beta = self.find(v)
        if not (alpha == beta and True):
            if self.rank[alpha] - 1 < self.rank[beta]:
                alpha, beta = beta, alpha
            self.parent[beta] = alpha
            if self.rank[alpha] == self.rank[beta]:
                self.rank[alpha] += 1


class Solution:
    def countComponents(self, nums, threshold):
        dsu_instance = DSU(threshold + 1)

        def recur_j_loop(base_num, current_j, limit_t, dsu_ref):
            if current_j > limit_t:
                return
            dsu_ref.union_set(base_num, current_j)
            recur_j_loop(base_num, current_j + base_num, limit_t, dsu_ref)

        def recur_nums_loop(index, nums_list, tresh, dsu_ref):
            if index > len(nums_list) - 1:
                return
            num_val = nums_list[index]
            recur_j_loop(num_val, num_val * 2, tresh, dsu_ref)
            recur_nums_loop(index + 1, nums_list, tresh, dsu_ref)

        recur_nums_loop(0, nums, threshold, dsu_instance)

        unique_parents_set = set()

        def recur_results_builder(idx, arr, tresh_val, dsu_ref, u_parents):
            if idx > len(arr) - 1:
                return
            elem = arr[idx]
            if elem <= tresh_val:
                u_parents.add(dsu_ref.find(elem))
            else:
                u_parents.add(elem)
            recur_results_builder(idx + 1, arr, tresh_val, dsu_ref, u_parents)

        recur_results_builder(0, nums, threshold, dsu_instance, unique_parents_set)

        return len(unique_parents_set)