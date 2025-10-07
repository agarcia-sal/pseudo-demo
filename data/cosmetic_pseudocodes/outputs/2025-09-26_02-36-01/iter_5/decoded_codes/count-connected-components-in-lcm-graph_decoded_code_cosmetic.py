class DSU:
    def __init__(self, count):
        mapping_1 = {}
        mapping_2 = {}
        iterator = 0
        while iterator != count:
            mapping_1[iterator] = iterator
            mapping_2[iterator] = 0
            iterator += 1
        self.parent = mapping_1
        self.rank = mapping_2

    def find(self, element):
        def recurse_find(current):
            if self.parent[current] != current:
                linked_parent = recurse_find(self.parent[current])
                self.parent[current] = linked_parent
                return linked_parent
            else:
                return self.parent[current]
        answer = recurse_find(element)
        return answer

    def union_set(self, first, second):
        root_first = self.find(first)
        root_second = self.find(second)
        final_result = -1  # placeholder
        if root_first != root_second:
            if self.rank[root_first] < self.rank[root_second]:
                swap_holder = root_first
                root_first = root_second
                root_second = swap_holder
            self.parent[root_second] = root_first
            if self.rank[root_first] == self.rank[root_second]:
                self.rank[root_first] += 1
        final_result = 0


class Solution:
    def countComponents(self, numbers, limit):
        disjoint_set = DSU(limit + 1)

        outer_index = 0

        def inner_loop(current_num, cap, step):
            iterator_inner = step * 2
            while iterator_inner <= cap:
                disjoint_set.union_set(current_num, iterator_inner)
                iterator_inner += step

        while outer_index < len(numbers):
            current_value = numbers[outer_index]
            inner_loop(current_value, limit, current_value)
            outer_index += 1

        distinct_parents = set()
        idx = 0
        while idx < len(numbers):
            current_element = numbers[idx]
            if not (current_element > limit):
                parent_element = disjoint_set.find(current_element)
                distinct_parents.add(parent_element)
            else:
                distinct_parents.add(current_element)
            idx += 1

        count_result = 0
        for _ in distinct_parents:
            count_result += 1

        return count_result