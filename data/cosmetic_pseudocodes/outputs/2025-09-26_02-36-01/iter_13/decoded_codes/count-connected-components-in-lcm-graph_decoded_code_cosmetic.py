from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = [0] * n
        self.rank = [0] * n
        def init_recursion(i: int):
            if i > n - 1:
                return
            self.parent[i] = i
            self.rank[i] = 0
            init_recursion(i + 1)
        init_recursion(0)

    def find(self, x: int) -> int:
        def finder(y: int) -> int:
            if self.parent[y] != y:
                temp_val = finder(self.parent[y])
                self.parent[y] = temp_val
            return self.parent[y]
        return finder(x)

    def union_set(self, u: int, v: int) -> None:
        u_inner = self.find(u)
        v_inner = self.find(v)
        if u_inner != v_inner:
            if self.rank[u_inner] < self.rank[v_inner]:
                u_inner, v_inner = v_inner, u_inner  # Swap to ensure u_inner has higher rank
            self.parent[v_inner] = u_inner
            if self.rank[u_inner] == self.rank[v_inner]:
                self.rank[u_inner] += 1

class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        def multiply_seq(val: int, limit: int, step: int) -> List[int]:
            result_list = []
            current = val + val
            def tail_recursion(c: int):
                if c > limit:
                    return
                result_list.append(c)
                tail_recursion(c + step)
            tail_recursion(current)
            return result_list

        dsu = DSU(threshold + 1)

        def recursive_outer(i: int):
            if i > len(nums) - 1:
                return
            num = nums[i]
            multiples = multiply_seq(num, threshold, num)
            def iterative(j: int):
                idx = j
                while idx < len(multiples):
                    self_union_left = num
                    self_union_right = multiples[idx]
                    dsu.union_set(self_union_left, self_union_right)
                    idx += 1
            iterative(0)
            recursive_outer(i + 1)
        recursive_outer(0)

        unique_parents = set()
        def for_set(i: int):
            if i >= len(nums):
                return
            cur_num = nums[i]
            if cur_num <= threshold:
                unique_parents.add(dsu.find(cur_num))
            else:
                unique_parents.add(cur_num)
            for_set(i + 1)
        for_set(0)

        return len(unique_parents)