class DSU:
    def __init__(self, length):
        self.parent = {}
        self.rank = {}
        counter = 0
        while counter < length:
            self.parent[counter] = counter
            self.rank[counter] = 0
            counter += 1

    def find(self, element):
        representative = self.parent[element]
        if representative != element:
            self.parent[element] = self.find(representative)
        return self.parent[element]

    def union_set(self, first, second):
        first_root = self.find(first)
        second_root = self.find(second)
        if first_root != second_root:
            if self.rank[first_root] < self.rank[second_root]:
                first_root, second_root = second_root, first_root
            self.parent[second_root] = first_root
            if self.rank[first_root] == self.rank[second_root]:
                self.rank[first_root] += 1


class Solution:
    def countComponents(self, numbers, limit):
        dsu = DSU(limit + 1)

        index = 0
        n = len(numbers)
        while index < n:
            current = numbers[index]
            multiple = current + current
            while multiple <= limit:
                dsu.union_set(current, multiple)
                multiple += current
            index += 1

        distinct_roots = set()
        for candidate in numbers:
            if candidate > limit:
                distinct_roots.add(candidate)
            else:
                distinct_roots.add(dsu.find(candidate))

        return len(distinct_roots)