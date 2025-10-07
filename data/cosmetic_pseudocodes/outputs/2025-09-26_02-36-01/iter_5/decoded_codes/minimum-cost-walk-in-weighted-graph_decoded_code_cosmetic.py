class UnionFind:
    def __init__(self, n):
        progenitors = []
        levels = []
        baseValue = 0
        upperLimit = n - 1
        while baseValue <= upperLimit:
            progenitors.append(baseValue)
            levels.append(1)
            baseValue += 1
        self.parent = progenitors
        self.rank = levels

    def find(self, position):
        currentRoot = self.parent[position]
        if currentRoot != position:
            updatedRoot = self.find(currentRoot)
            self.parent[position] = updatedRoot
            currentRoot = updatedRoot
        return currentRoot

    def union(self, alpha, beta):
        rootAlpha = self.find(alpha)
        rootBeta = self.find(beta)
        if rootAlpha != rootBeta:
            rankAlpha = self.rank[rootAlpha]
            rankBeta = self.rank[rootBeta]
            if rankAlpha > rankBeta:
                self.parent[rootBeta] = rootAlpha
            elif rankAlpha < rankBeta:
                self.parent[rootAlpha] = rootBeta
            else:
                self.parent[rootBeta] = rootAlpha
                self.rank[rootAlpha] = rankAlpha + 1


class Solution:
    def minimumCost(self, count, edges, query):
        ufInstance = UnionFind(count)
        allBitsMask = (1 << 32) - 1
        accComponents = []
        idxCounter = 0
        while idxCounter < count:
            accComponents.append(allBitsMask)
            idxCounter += 1

        edgeIdx = 0
        while edgeIdx < len(edges):
            edgeTriple = edges[edgeIdx]
            localU = edgeTriple[0]
            localV = edgeTriple[1]
            localW = edgeTriple[2]
            ufInstance.union(localU, localV)
            componentID = ufInstance.find(localU)
            accComponents[componentID] = accComponents[componentID] & localW
            edgeIdx += 1

        costsDict = {}
        i = 0
        while i < count:
            leader = ufInstance.find(i)
            if leader not in costsDict:
                costsDict[leader] = accComponents[leader]
            i += 1

        outputList = []
        qIdx = 0
        totalQueries = len(query)
        while qIdx < totalQueries:
            pairElement = query[qIdx]
            startNode = pairElement[0]
            targetNode = pairElement[1]
            if startNode == targetNode:
                answer = 0
            else:
                rootStart = ufInstance.find(startNode)
                rootTarget = ufInstance.find(targetNode)
                if rootStart == rootTarget:
                    answer = costsDict[rootStart]
                else:
                    answer = -1
            outputList.append(answer)
            qIdx += 1

        return outputList