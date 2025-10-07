class UnionFind:
    def __init__(self, total):
        self.parent = list(range(total))
        self.rank = [1] * total

    def find(self, element):
        while self.parent[element] != element:
            self.parent[element] = self.parent[self.parent[element]]
            element = self.parent[element]
        return element

    def union(self, first, second):
        rootFirst = self.find(first)
        rootSecond = self.find(second)
        if rootFirst != rootSecond:
            if self.rank[rootFirst] > self.rank[rootSecond]:
                self.parent[rootSecond] = rootFirst
            elif self.rank[rootFirst] < self.rank[rootSecond]:
                self.parent[rootFirst] = rootSecond
            else:
                self.parent[rootSecond] = rootFirst
                self.rank[rootFirst] += 1


class Solution:
    def minimumCost(self, count, connections, queries):
        uf = UnionFind(count)
        maxValue = (1 << 32) - 1
        componentsMask = [maxValue] * count

        for edge in connections:
            nodeA, nodeB, weight = edge
            uf.union(nodeA, nodeB)
            rootNode = uf.find(nodeA)
            componentsMask[rootNode] &= weight

        compCostMap = {}
        for index in range(count):
            rootId = uf.find(index)
            if rootId not in compCostMap:
                compCostMap[rootId] = componentsMask[rootId]

        answerList = []
        for startNode, endNode in queries:
            if startNode == endNode:
                answerList.append(0)
            else:
                ancestorStart = uf.find(startNode)
                ancestorEnd = uf.find(endNode)
                if ancestorStart == ancestorEnd:
                    answerList.append(compCostMap[ancestorStart])
                else:
                    answerList.append(-1)
        return answerList