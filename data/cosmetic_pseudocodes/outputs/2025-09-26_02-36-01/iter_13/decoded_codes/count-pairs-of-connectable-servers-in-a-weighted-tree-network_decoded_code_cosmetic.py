from collections import defaultdict

class Solution:
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        graph = defaultdict(list)

        def insertPair(gm, a, b, c):
            gm[a].append((b, c))

        def addEdges(edgeList, graphMap):
            for idx in range(1, len(edgeList)):
                x, y, z = edgeList[idx]
                insertPair(graphMap, x, y, z)
                insertPair(graphMap, y, x, z)

        addEdges(edges, graph)
        nodeCount = len(graph)
        outputArray = [0] * nodeCount

        def dfs(currentNode, parentNode, distAcc, collectedPath):
            divisibleCondition = (distAcc % signalSpeed) == 0
            if divisibleCondition:
                collectedPath.append(currentNode)
            accumulator = 0

            def recurNeighbors(idx):
                if idx > len(graph[currentNode]):
                    return 0
                neigh, wgt = graph[currentNode][idx - 1]
                if neigh != parentNode:
                    callResult = dfs(neigh, currentNode, distAcc + wgt, collectedPath)
                    return callResult + recurNeighbors(idx + 1)
                else:
                    return recurNeighbors(idx + 1)

            accumulator = recurNeighbors(1)
            if divisibleCondition:
                return accumulator + 1
            else:
                return accumulator

        def count_pairs_through_c(centerNode):
            allPaths = []

            def gatherPathsList(idx):
                if idx > len(graph[centerNode]):
                    return
                nbr, wgt = graph[centerNode][idx - 1]
                singlePath = []
                dfs(nbr, centerNode, wgt, singlePath)
                allPaths.append(singlePath)
                gatherPathsList(idx + 1)

            gatherPathsList(1)
            pairsCount = 0
            pathNum = len(allPaths)

            def pairwiseSum(i, j):
                nonlocal pairsCount
                if i >= pathNum:
                    return
                if j >= pathNum:
                    pairwiseSum(i + 1, i + 2)
                    return
                pairsCount += len(allPaths[i]) * len(allPaths[j])
                pairwiseSum(i, j + 1)

            pairwiseSum(0, 1)
            return pairsCount

        def assignResults(index):
            if index >= nodeCount:
                return
            outputArray[index] = count_pairs_through_c(index)
            assignResults(index + 1)

        assignResults(0)
        return outputArray