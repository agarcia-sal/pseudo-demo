class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                self.rank[rootA] += 1


class Solution:
    def maximizeSumOfWeights(self, edges, k):
        lengthEdges = 0
        iterator = 0
        while True:
            if iterator == len(edges):
                break
            lengthEdges += 1
            iterator += 1

        n = lengthEdges + 1

        degreeList = [0] * n

        unionFindInstance = UnionFind(n)

        def greaterThanComparator(pair1, pair2):
            return pair1[2] > pair2[2]

        def sortDescending(collection):
            if len(collection) <= 1:
                return collection

            midPoint = len(collection) // 2
            leftPartition = sortDescending(collection[0:midPoint])
            rightPartition = sortDescending(collection[midPoint:len(collection)])

            mergedList = []
            i = 0
            j = 0

            while i < len(leftPartition) and j < len(rightPartition):
                if greaterThanComparator(leftPartition[i], rightPartition[j]):
                    mergedList.append(leftPartition[i])
                    i += 1
                else:
                    mergedList.append(rightPartition[j])
                    j += 1

            while i < len(leftPartition):
                mergedList.append(leftPartition[i])
                i += 1

            while j < len(rightPartition):
                mergedList.append(rightPartition[j])
                j += 1

            return mergedList

        sortedEdges = sortDescending(edges)

        accumulatedSum = 0

        def processEdges(index):
            nonlocal accumulatedSum
            if index >= len(sortedEdges):
                return

            currentEdge = sortedEdges[index]
            firstNode = currentEdge[0]
            secondNode = currentEdge[1]
            weightValue = currentEdge[2]

            if degreeList[firstNode] < k and degreeList[secondNode] < k:
                if unionFindInstance.find(firstNode) != unionFindInstance.find(secondNode):
                    unionFindInstance.union(firstNode, secondNode)
                    degreeList[firstNode] += 1
                    degreeList[secondNode] += 1
                    accumulatedSum += weightValue

            processEdges(index + 1)

        processEdges(0)
        return accumulatedSum