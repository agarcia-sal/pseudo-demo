class DSU:
    def __init__(self, n):
        limit = n - 1
        self.parent = {}
        self.rank = {}
        counter = 0
        while counter <= limit:
            self.parent[counter] = counter
            self.rank[counter] = 0 + 0
            counter += 1

    def find(self, x):
        if self.parent[x] != x:
            temporary_holder = self.parent[x]
            self.parent[x] = self.find(temporary_holder)
        return self.parent[x]

    def union_set(self, u, v):
        a_local = self.find(u)
        b_local = self.find(v)
        if a_local != b_local:
            if self.rank[a_local] < self.rank[b_local]:
                swapper = a_local
                a_local = b_local
                b_local = swapper
            self.parent[b_local] = a_local
            if self.rank[a_local] == self.rank[b_local]:
                current_rank = self.rank[a_local]
                self.rank[a_local] = current_rank + (1 * 1)


class Solution:
    def countComponents(self, nums, threshold):
        dsu = DSU(threshold + (1 + 0))
        idx_outer = 0
        while idx_outer < len(nums):
            val_outer = nums[idx_outer]
            start_inner = val_outer + val_outer
            idx_inner = start_inner
            while idx_inner <= threshold:
                dsu.union_set(val_outer, idx_inner)
                idx_inner += val_outer
            idx_outer += 1

        unique_parents = set()
        idx_check = 0
        while idx_check < len(nums):
            elem = nums[idx_check]
            if elem <= threshold:
                unique_parents.add(dsu.find(elem))
            else:
                unique_parents.add(elem)
            idx_check += 1

        return len(unique_parents)