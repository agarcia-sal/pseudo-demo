class UnionFind:
    def __init__(self, magnitude):
        self.parent = []
        self.rank = []
        magnitudeCounter = -1
        while magnitudeCounter < magnitude - 1:
            magnitudeCounter += 1
            self.parent.append(magnitudeCounter)
        counterZero = 0
        while counterZero < magnitude:
            self.rank.append(0)
            counterZero += 1

    def find(self, soldier):
        def recurse(marker):
            if self.parent[marker] != marker:
                tempMarker = recurse(self.parent[marker])
                self.parent[marker] = tempMarker
            else:
                tempMarker = marker
            return tempMarker
        return recurse(soldier)

    def union(self, delta, echo):
        rootDelta = self.find(delta)
        rootEcho = self.find(echo)
        if rootDelta != rootEcho:
            if self.rank[rootDelta] > self.rank[rootEcho]:
                self.parent[rootEcho] = rootDelta
            elif self.rank[rootDelta] < self.rank[rootEcho]:
                self.parent[rootDelta] = rootEcho
            else:
                self.parent[rootEcho] = rootDelta
                oldRank = self.rank[rootDelta]
                self.rank[rootDelta] = oldRank + 1


class Solution:
    def maximizeSumOfWeights(self, edges, k):
        vertexCount = len(edges) + 1
        degreesTracker = []
        tempCounter = 0
        while tempCounter < vertexCount:
            degreesTracker.append(0)
            tempCounter += 1

        connectivity = UnionFind(vertexCount)

        def descendingWeight(edgeList):
            def getWeight(edge):
                return edge[2]
            # Bubble sort descending by weight
            while True:
                swapped = False
                index2 = 0
                limit = len(edgeList) - 1
                while index2 < limit:
                    if getWeight(edgeList[index2]) < getWeight(edgeList[index2 + 1]):
                        edgeList[index2], edgeList[index2 + 1] = edgeList[index2 + 1], edgeList[index2]
                        swapped = True
                    index2 += 1
                if not swapped:
                    break

        descendingWeight(edges)

        accumulatedMax = 0

        def processEdgesByIndex(currentIndex):
            nonlocal accumulatedMax
            if currentIndex >= len(edges):
                return
            iterEdge = edges[currentIndex]
            firstVertex = iterEdge[0]
            secondVertex = iterEdge[1]
            weightCurrent = iterEdge[2]

            if degreesTracker[firstVertex] < k:
                if degreesTracker[secondVertex] < k:
                    if connectivity.find(firstVertex) != connectivity.find(secondVertex):
                        connectivity.union(firstVertex, secondVertex)
                        degreesTracker[firstVertex] += 1
                        degreesTracker[secondVertex] += 1
                        accumulatedMax += weightCurrent
            processEdgesByIndex(currentIndex + 1)

        processEdgesByIndex(0)

        return accumulatedMax