class DSU:
    def __init__(self, z: int):
        self.parent = {i: i for i in range(z)}
        self.rank = {i: 0 for i in range(z)}

    def find(self, Y: int) -> int:
        if self.parent[Y] != Y:
            self.parent[Y] = self.find(self.parent[Y])
        return self.parent[Y]

    def union_set(self, B: int, C: int) -> None:
        P = self.find(B)
        R = self.find(C)
        if P != R:
            if self.rank[P] < self.rank[R]:
                P, R = R, P
            self.parent[R] = P
            if self.rank[P] == self.rank[R]:
                self.rank[P] += 1


class Solution:
    def countComponents(self, L: list[int], h: int) -> int:
        structure = DSU(h + 1)

        for val in L:
            multiplier = val * 2
            while multiplier <= h:
                structure.union_set(val, multiplier)
                multiplier += val

        parents_set = set()
        for item in L:
            if item <= h:
                parents_set.add(structure.find(item))
            else:
                parents_set.add(item)

        return len(parents_set)