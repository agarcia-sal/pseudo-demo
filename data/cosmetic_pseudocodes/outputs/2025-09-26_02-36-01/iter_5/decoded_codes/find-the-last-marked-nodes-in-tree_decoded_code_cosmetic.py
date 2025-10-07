class Solution:
    def lastMarkedNodes(self, edges):
        def dfs(node, parent, distances):
            neighbours = g[node]
            idx = 0
            while idx < len(neighbours):
                neighborNode = neighbours[idx]
                if neighborNode != parent:
                    distances[neighborNode] = distances[node] + 1
                    dfs(neighborNode, node, distances)
                idx += 1

        nodeCount = len(edges) + 1
        g = []
        buildIndex = 0
        while buildIndex < nodeCount:
            g.append([])
            buildIndex += 1

        edgeCounter = 0
        while edgeCounter < len(edges):
            pair = edges[edgeCounter]
            firstNode, secondNode = pair[0], pair[1]
            g[firstNode].append(secondNode)
            g[secondNode].append(firstNode)
            edgeCounter += 1

        distancesFromZero = []
        fillIndex = 0
        while fillIndex < nodeCount:
            distancesFromZero.append(-1)
            fillIndex += 1
        distancesFromZero[0] = 0
        dfs(0, -1, distancesFromZero)

        maxDistance = -1
        posA = 0
        checkIndex = 0
        while checkIndex < nodeCount:
            if maxDistance < distancesFromZero[checkIndex]:
                maxDistance = distancesFromZero[checkIndex]
                posA = checkIndex
            checkIndex += 1

        distancesFromA = []
        fillIndex2 = 0
        while fillIndex2 < nodeCount:
            distancesFromA.append(-1)
            fillIndex2 += 1
        distancesFromA[posA] = 0
        dfs(posA, -1, distancesFromA)

        maxDistance2 = -1
        posB = 0
        checkIndex2 = 0
        while checkIndex2 < nodeCount:
            if maxDistance2 < distancesFromA[checkIndex2]:
                maxDistance2 = distancesFromA[checkIndex2]
                posB = checkIndex2
            checkIndex2 += 1

        distancesFromB = []
        fillIndex3 = 0
        while fillIndex3 < nodeCount:
            distancesFromB.append(-1)
            fillIndex3 += 1
        distancesFromB[posB] = 0
        dfs(posB, -1, distancesFromB)

        outputList = []
        idxOut = 0
        while idxOut < nodeCount:
            valFromA = distancesFromA[idxOut]
            valFromB = distancesFromB[idxOut]
            if valFromA > valFromB:
                outputList.append(posA)
            else:
                outputList.append(posB)
            idxOut += 1

        resultValue = outputList
        return resultValue