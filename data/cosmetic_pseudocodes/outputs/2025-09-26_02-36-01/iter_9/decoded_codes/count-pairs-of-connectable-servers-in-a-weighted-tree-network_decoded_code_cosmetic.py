from collections import defaultdict
from typing import List, Tuple


class Solution:
    def countPairsOfConnectableServers(self, edges: List[Tuple[int, int, int]], signalSpeed: int) -> List[int]:
        def makeAdjacencyMap(edgeList: List[Tuple[int, int, int]]):
            adjacency = defaultdict(list)

            def addEdge(x: int, y: int, weight: int):
                adjacency[x].append((y, weight))

            index = 0
            while index < len(edgeList):
                currentEdge = edgeList[index]
                addEdge(currentEdge[0], currentEdge[1], currentEdge[2])
                addEdge(currentEdge[1], currentEdge[0], currentEdge[2])
                index += 1
            return adjacency

        graphMap = makeAdjacencyMap(edges)

        # totalNodes is the count of distinct nodes observed in the graph
        totalNodes = len(graphMap)

        resultList = [0] * totalNodes

        def isDivisible(dist: int, divisor: int) -> bool:
            return (dist % divisor) == 0

        def depthSearch(current: int, prev: int, distAcc: int, collectedPath: List[int]) -> int:
            if isDivisible(distAcc, signalSpeed):
                collectedPath.append(current)

            subtreeCount = 0
            neighborsList = graphMap[current]

            idxNeighbor = 0
            while idxNeighbor < len(neighborsList):
                nextNode, edgeWeight = neighborsList[idxNeighbor]
                if nextNode != prev:
                    subtreeCount += depthSearch(nextNode, current, distAcc + edgeWeight, collectedPath)
                idxNeighbor += 1

            if isDivisible(distAcc, signalSpeed):
                return subtreeCount + 1
            else:
                return subtreeCount

        def pairsCountCenter(centerNode: int) -> int:
            allPathsLists = []
            for neigh, w in graphMap[centerNode]:
                singlePath = []
                depthSearch(neigh, centerNode, w, singlePath)
                allPathsLists.append(singlePath)

            pairsTotal = 0
            outerIndex = 0
            while outerIndex < len(allPathsLists) - 1:
                innerIndex = outerIndex + 1
                while innerIndex < len(allPathsLists):
                    lengthProd = len(allPathsLists[outerIndex]) * len(allPathsLists[innerIndex])
                    pairsTotal += lengthProd
                    innerIndex += 1
                outerIndex += 1

            return pairsTotal

        indexNode = 0
        while indexNode < totalNodes:
            resultList[indexNode] = pairsCountCenter(indexNode)
            indexNode += 1

        return resultList