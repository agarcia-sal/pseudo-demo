from collections import defaultdict

class Solution:
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        adjacencyMap = defaultdict(list)

        def addEdge(a, b, cost):
            adjacencyMap[a].append((b, cost))
            adjacencyMap[b].append((a, cost))

        def buildGraphRec(idx):
            if idx == len(edges):
                return
            x, y, z = edges[idx]
            addEdge(x, y, z)
            buildGraphRec(idx + 1)
        buildGraphRec(0)

        nodeCount = len(adjacencyMap)
        outputList = [0] * nodeCount

        def explore(currentNode, prevNode, dist, collectedPath):
            modValue = dist % signalSpeed
            if modValue == 0:
                collectedPath.append(currentNode)

            def exploreNeighbors(idx):
                if idx == len(adjacencyMap[currentNode]):
                    return 0
                nextNode, edgeWeight = adjacencyMap[currentNode][idx]
                if nextNode != prevNode:
                    recurseCount = explore(nextNode, currentNode, dist + edgeWeight, collectedPath)
                    afterCount = exploreNeighbors(idx + 1)
                    return recurseCount + afterCount
                else:
                    return exploreNeighbors(idx + 1)

            neighborTotals = exploreNeighbors(0)
            return neighborTotals + 1 if modValue == 0 else neighborTotals

        def pairsCountForNode(centerNode):
            allPaths = []

            def collectPaths(idx):
                if idx == len(adjacencyMap[centerNode]):
                    return
                adjNode, weight = adjacencyMap[centerNode][idx]
                pathContainer = []
                explore(adjNode, centerNode, weight, pathContainer)
                allPaths.append(pathContainer)
                collectPaths(idx + 1)
            collectPaths(0)

            pairsTotal = 0

            def computePairs(i):
                nonlocal pairsTotal
                if i == len(allPaths):
                    return

                def innerLoop(j):
                    nonlocal pairsTotal
                    if j == len(allPaths):
                        return
                    pairsTotal += len(allPaths[i]) * len(allPaths[j])
                    innerLoop(j + 1)

                innerLoop(i + 1)
                computePairs(i + 1)
            computePairs(0)

            return pairsTotal

        def fillResult(k):
            if k == nodeCount:
                return
            pairCount = pairsCountForNode(k)
            outputList[k] = pairCount
            fillResult(k + 1)
        fillResult(0)

        return outputList