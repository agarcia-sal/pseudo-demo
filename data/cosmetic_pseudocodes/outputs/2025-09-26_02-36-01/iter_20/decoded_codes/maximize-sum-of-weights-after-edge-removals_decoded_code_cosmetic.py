class UnionFind:
    def __init__(self, size):
        p = [0] * size
        r = [0] * size
        m = 0
        while m <= size - 1:
            p[m] = m
            m += 1
        self.parent = p
        self.rank = r

    def find(self, u):
        def recFind(x):
            if self.parent[x] != x:
                y = recFind(self.parent[x])
                self.parent[x] = y
                return y
            else:
                return x
        return recFind(u)

    def union(self, u, v):
        a = self.find(u)
        b = self.find(v)
        if a != b:
            if self.rank[a] > self.rank[b]:
                self.parent[b] = a
            else:
                if self.rank[a] < self.rank[b]:
                    self.parent[a] = b
                else:
                    self.parent[b] = a
                    self.rank[a] += 1


class Solution:
    def maximizeSumOfWeights(self, edges, k):
        x = len(edges)
        n = x + 1
        deg = [0] * n
        uf = UnionFind(n)

        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            j = low
            while j <= high - 1:
                if arr[j][2] >= pivot[2]:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                j += 1
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def quicksort(arr, l, h):
            if l >= h:
                return
            pidx = partition(arr, l, h)
            quicksort(arr, l, pidx - 1)
            quicksort(arr, pidx + 1, h)

        quicksort(edges, 0, x - 1)

        total = 0

        def processEdges(i):
            nonlocal total
            if i >= x:
                return
            currEdge = edges[i]
            a, b, w = currEdge[0], currEdge[1], currEdge[2]
            if deg[a] < k and deg[b] < k:
                fa = uf.find(a)
                fb = uf.find(b)
                if fa != fb:
                    uf.union(a, b)
                    deg[a] += 1
                    deg[b] += 1
                    total += w
            processEdges(i + 1)

        processEdges(0)

        return total