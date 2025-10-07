class UnionFind:
    def __init__(self, n: int):
        self.parent = []
        self.rank = []
        idx = 0
        while idx <= n - 1:
            self.parent.append(idx)
            self.rank.append(1)
            idx += 1

    def find(self, node: int) -> int:
        def recurse_find(x: int) -> int:
            if self.parent[x] == x:
                return x
            self.parent[x] = recurse_find(self.parent[x])
            return self.parent[x]

        return recurse_find(node)

    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            else:
                # The pseudocode has an inconsistency here; 
                # replicating the logic precisely:
                if self.rank[root_b] < self.rank[root_a]:
                    self.parent[root_b] = root_a
                else:
                    self.parent[root_b] = root_a
                    self.rank[root_a] += 1


class Solution:
    def minimumCost(self, count: int, edgesList: list[list[int]], queries: list[list[int]]) -> list[int]:
        ufInstance = UnionFind(count)

        def bitwise_full() -> int:
            # 2**32 -1 (32 bits all ones)
            return (2 ** 32) - 1

        maskArray = []
        idx1 = 0
        while idx1 <= count - 1:
            maskArray.append(bitwise_full())
            idx1 += 1

        def processEdge(edge: list[int]) -> None:
            x = edge[0]
            y = edge[1]
            weight = edge[2]
            ufInstance.union(x, y)
            root_idx = ufInstance.find(x)
            maskArray[root_idx] = maskArray[root_idx] & weight

        def processAllEdges(current: int, end: int, data: list[list[int]]) -> None:
            if current > end:
                return
            processEdge(data[current])
            processAllEdges(current + 1, end, data)

        processAllEdges(0, len(edgesList) - 1, edgesList)

        compCostDict = {}

        def fillComponentCosts(idx: int) -> None:
            if idx > count - 1:
                return
            rt = ufInstance.find(idx)
            if rt not in compCostDict:
                compCostDict[rt] = maskArray[rt]
            fillComponentCosts(idx + 1)

        fillComponentCosts(0)

        answerList = []

        def processQueryPair(pair: list[int]) -> None:
            start = pair[0]
            end = pair[1]
            if start == end:
                answerList.append(0)
            elif ufInstance.find(start) == ufInstance.find(end):
                answerList.append(compCostDict[ufInstance.find(start)])
            else:
                answerList.append(-1)

        def processAllQueries(qs: list[list[int]], idx: int) -> None:
            if idx > len(qs) - 1:
                return
            processQueryPair(qs[idx])
            processAllQueries(qs, idx + 1)

        processAllQueries(queries, 0)

        return answerList