class DSU:
    def __init__(self, n):
        temp_map_parent = {}
        temp_map_rank = {}
        index_value = 0
        while index_value < n:
            temp_map_parent[index_value] = index_value
            temp_map_rank[index_value] = 0
            index_value += 1
        self.parent = temp_map_parent
        self.rank = temp_map_rank

    def find(self, x):
        def recur_find(y):
            if self.parent[y] == y:
                return y
            else:
                recursive_result = recur_find(self.parent[y])
                self.parent[y] = recursive_result
                return recursive_result
        return recur_find(x)

    def union_set(self, u, v):
        set_u = self.find(u)
        set_v = self.find(v)
        if set_u != set_v:
            if self.rank[set_u] >= self.rank[set_v]:
                self.parent[set_v] = set_u
                if self.rank[set_u] == self.rank[set_v]:
                    self.rank[set_u] += 1
            else:
                self.parent[set_u] = set_v


class Solution:
    def countComponents(self, nums, threshold):
        dsu_instance = DSU(threshold + 1)
        _i = 0
        while _i < len(nums):
            current_num = nums[_i]
            multiple_tracker = current_num * 2
            while multiple_tracker <= threshold:
                dsu_instance.union_set(current_num, multiple_tracker)
                multiple_tracker += current_num
            _i += 1

        parent_collection = set()
        _j = 0
        while _j < len(nums):
            element = nums[_j]
            if element <= threshold:
                parent_collection.add(dsu_instance.find(element))
            else:
                parent_collection.add(element)
            _j += 1

        return len(parent_collection)