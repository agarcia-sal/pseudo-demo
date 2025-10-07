class DSU:
    def __init__(self, count):
        self.parent = {i: i for i in range(count)}
        self.rank = {i: 0 for i in range(count)}

    def find(self, element):
        def helper_find(key):
            if self.parent[key] != key:
                self.parent[key] = helper_find(self.parent[key])
            return self.parent[key]
        return helper_find(element)

    def union_set(self, first, second):
        x = self.find(first)
        y = self.find(second)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


class Solution:
    def countComponents(self, arr, limit):
        data_structure = DSU(limit + 1)

        outer_index = 0
        while outer_index < len(arr):
            value = arr[outer_index]
            inner_value = value * 2
            while inner_value <= limit:
                data_structure.union_set(value, inner_value)
                inner_value += value
            outer_index += 1

        collector_set = set()
        gather_index = 0
        while gather_index < len(arr):
            curr_val = arr[gather_index]
            if curr_val <= limit:
                collector_set.add(data_structure.find(curr_val))
            else:
                collector_set.add(curr_val)
            gather_index += 1

        def set_size(s):
            count_items = 0
            for _ in s:
                count_items += 1
            return count_items

        return set_size(collector_set)