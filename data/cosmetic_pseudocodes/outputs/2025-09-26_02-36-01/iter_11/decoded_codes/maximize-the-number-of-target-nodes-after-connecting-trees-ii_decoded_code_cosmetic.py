from collections import defaultdict
from typing import List, Tuple

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        containerAlpha = defaultdict(list)
        containerBeta = defaultdict(list)

        def addConnection(graph: defaultdict, node1: int, node2: int) -> None:
            graph[node1].append(node2)

        def insertEdges(edgeList: List[List[int]], adjacency: defaultdict) -> None:
            for edge in edgeList:
                firstNode, secondNode = edge
                addConnection(adjacency, firstNode, secondNode)
                addConnection(adjacency, secondNode, firstNode)

        insertEdges(edges1, containerAlpha)
        insertEdges(edges2, containerBeta)

        countAlpha = len(containerAlpha)
        countBeta = len(containerBeta)

        def exploreLevels(graphStructure: defaultdict, origin: int) -> Tuple[int, int]:
            countEven = 0
            countOdd = 0

            frontier = [(origin, 0)]
            seenNodes = {origin}

            def dequeuePop(dequeStructure: List[Tuple[int, int]]) -> Tuple[int, int]:
                element = dequeStructure[0]
                del dequeStructure[0]
                return element

            def loopFrontier() -> None:
                nonlocal countEven, countOdd
                if len(frontier) == 0:
                    return

                currentNode, distanceValue = dequeuePop(frontier)

                if distanceValue % 2 == 0:
                    countEven += 1
                else:
                    countOdd += 1

                def examineNeighbors(nodesList: List[int]) -> None:
                    if not nodesList:
                        return

                    neighbor = nodesList[0]
                    del nodesList[0]

                    if neighbor not in seenNodes:
                        seenNodes.add(neighbor)
                        frontier.append((neighbor, distanceValue + 1))

                    examineNeighbors(nodesList)

                neighbors = graphStructure.get(currentNode, []).copy()
                examineNeighbors(neighbors)
                loopFrontier()

            loopFrontier()

            return countEven, countOdd

        listCountsA = []

        def generateCountsA(idx: int, limit: int) -> None:
            if idx == limit:
                return
            listCountsA.append(exploreLevels(containerAlpha, idx))
            generateCountsA(idx + 1, limit)

        generateCountsA(0, countAlpha)

        listCountsB = []
        for iterator in range(countBeta):
            tempPair = exploreLevels(containerBeta, iterator)
            listCountsB.append(tempPair)

        compilation = []

        def combineCounts(x: int, upperBound: int) -> None:
            if x == upperBound:
                return

            evenAlpha, oddAlpha = listCountsA[x]
            highestTargets = 0

            def checkCandidates(y: int, bound: int) -> None:
                nonlocal highestTargets
                if y == bound:
                    return
                evenBeta, oddBeta = listCountsB[y]
                if x == y or ((x % 2) == (y % 2)):
                    localMax = evenBeta
                else:
                    localMax = oddBeta

                if localMax > highestTargets:
                    highestTargets = localMax

                checkCandidates(y + 1, bound)

            checkCandidates(0, countBeta)
            compilation.append(evenAlpha + highestTargets)
            combineCounts(x + 1, upperBound)

        combineCounts(0, countAlpha)

        return compilation