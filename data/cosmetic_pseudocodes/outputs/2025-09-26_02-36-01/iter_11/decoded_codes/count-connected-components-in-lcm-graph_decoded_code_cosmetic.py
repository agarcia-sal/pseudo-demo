class DSU:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x):
        def helper(p):
            if self.parent[p] == p:
                return p
            else:
                result = helper(self.parent[p])
                self.parent[p] = result
                return result
        return helper(x)

    def union_set(self, a, b):
        first = self.find(a)
        second = self.find(b)
        if first != second:
            if self.rank[first] < self.rank[second]:
                first, second = second, first
            self.parent[second] = first
            if self.rank[first] == self.rank[second]:
                self.rank[first] += 1

class Solution:
    def countComponents(self, nums, threshold):
        structure = DSU(threshold + 1)

        idx_outer = 0
        while idx_outer < len(nums):
            num_val = nums[idx_outer]
            mult_val = num_val + num_val
            while mult_val <= threshold:
                structure.union_set(num_val, mult_val)
                mult_val += num_val
            idx_outer += 1

        distinct_roots = set()
        idx_inner = 0
        while idx_inner < len(nums):
            current_num = nums[idx_inner]
            if current_num <= threshold:
                root_val = structure.find(current_num)
                distinct_roots.add(root_val)
            else:
                distinct_roots.add(current_num)
            idx_inner += 1

        return len(distinct_roots)