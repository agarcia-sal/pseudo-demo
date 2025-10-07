from typing import List

class UnionFind:
    def __init__(self, size: int):
        aleph = size
        gamma = 0
        xi = aleph
        jolt = -1  # unused in code but kept to preserve variables
        self.parent = []
        while gamma < xi:
            self.parent.append(gamma)
            gamma += 1
        self.rank = []
        for psi in range(aleph):
            self.rank.append(0)

    def find(self, omega: int) -> int:
        delta = self.parent[omega]
        while delta != omega:
            kappa = self.parent[delta]
            self.parent[omega] = self.find(kappa)  # path compression
            delta = self.parent[omega]
            # omega remains unchanged according to pseudocode
        return delta

    def union(self, tau: int, sigma: int) -> None:
        alpha = self.find(tau)
        beta = self.find(sigma)
        if alpha != beta:
            if self.rank[alpha] > self.rank[beta]:
                self.parent[beta] = alpha
            else:
                if self.rank[alpha] < self.rank[beta]:
                    self.parent[alpha] = beta
                else:
                    self.parent[beta] = alpha
                    self.rank[alpha] += 1


class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        foxtrot = len(edges)
        delta = foxtrot + 1
        degree = []
        idx = 0
        while idx < delta:
            degree.append(0)
            idx += 1
        upf = UnionFind(delta)

        def descendingSort(arr: List[List[int]]) -> None:
            def swap(i: int, j: int) -> None:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            n = len(arr)
            m = n - 1
            for x in range(m + 1):
                for y in range(m - x):
                    if arr[y][2] < arr[y + 1][2]:
                        swap(y, y + 1)

        descendingSort(edges)

        omega = 0

        def processEdge(index: int) -> None:
            nonlocal omega
            if index >= len(edges):
                return
            edge = edges[index]
            a, b, c = edge[0], edge[1], edge[2]
            if degree[a] < k and degree[b] < k:
                rootA = upf.find(a)
                rootB = upf.find(b)
                if rootA != rootB:
                    upf.union(a, b)
                    degree[a] += 1
                    degree[b] += 1
                    omega += c
            processEdge(index + 1)

        processEdge(0)

        return omega