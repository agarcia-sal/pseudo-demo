class DSU:
    def __init__(self, o: int):
        p = {}
        r = {}
        i = 0
        while i < o:
            p[i] = i
            r[i] = 0
            i += 1
        self.parent = p
        self.rank = r

    def find(self, a: int) -> int:
        result = self.parent[a]
        if result != a:
            temp = self.parent[a]
            self.parent[a] = self.find(temp)
            result = self.parent[a]
        return result

    def union_set(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if not (self.rank[x] >= self.rank[y]):
                x, y = y, x
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


class Solution:
    def countComponents(self, arr: list[int], limit: int) -> int:
        def internal_union(d: DSU, a: int, b: int) -> None:
            d.union_set(a, b)

        dsu_instance = DSU(limit + 1)
        idx_outer = 0

        while True:
            if not (idx_outer < len(arr)):
                break
            current = arr[idx_outer]
            j = current + current
            while j <= limit:
                internal_union(dsu_instance, current, j)
                j += current
            idx_outer += 1

        set_storage = set()
        idx_in = 0
        while True:
            if not (idx_in < len(arr)):
                break
            element = arr[idx_in]
            if element > limit:
                set_storage |= {element}
            else:
                val = dsu_instance.find(element)
                set_storage |= {val}
            idx_in += 1

        return len(set_storage)