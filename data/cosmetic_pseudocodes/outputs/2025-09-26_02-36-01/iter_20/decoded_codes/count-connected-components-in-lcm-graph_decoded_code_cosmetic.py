class DSU:
    def __init__(self, n):
        map_parent = {}
        map_rank = {}
        index_counter = 0
        while index_counter < n:
            map_parent[index_counter] = index_counter
            map_rank[index_counter] = 0
            index_counter += 1
        self.parent = map_parent
        self.rank = map_rank

    def find(self, x):
        def recurse(y):
            if self.parent[y] != y:
                temp_val = recurse(self.parent[y])
                self.parent[y] = temp_val
            return self.parent[y]
        return recurse(x)

    def union_set(self, u, v):
        rep_u = self.find(u)
        rep_v = self.find(v)
        if rep_u != rep_v:
            if self.rank[rep_u] < self.rank[rep_v]:
                rep_u, rep_v = rep_v, rep_u
            self.parent[rep_v] = rep_u
            if self.rank[rep_u] == self.rank[rep_v]:
                self.rank[rep_u] += 1


class Solution:
    def countComponents(self, nums, threshold):
        instance_dsu = DSU(threshold + 1)
        for num_item in nums:
            multiplier = 2
            while multiplier * num_item <= threshold:
                current_val = multiplier * num_item
                instance_dsu.union_set(num_item, current_val)
                multiplier += 1

        set_unique = set()
        index_iter = 0
        total_len = len(nums)
        while index_iter < total_len:
            iter_num = nums[index_iter]
            if iter_num <= threshold:
                parent_val = instance_dsu.find(iter_num)
                set_unique.add(parent_val)
            else:
                set_unique.add(iter_num)
            index_iter += 1

        return len(set_unique)