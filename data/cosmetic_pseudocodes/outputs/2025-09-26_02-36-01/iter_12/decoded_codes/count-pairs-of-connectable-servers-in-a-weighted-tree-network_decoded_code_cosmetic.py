from collections import defaultdict
from typing import List, Dict

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        graph: Dict[int, List[List[int]]] = defaultdict(list)

        def populateGraph(edgeEntries: List[List[int]], graphMap: Dict[int, List[List[int]]]) -> None:
            for uvwTriplet in edgeEntries:
                rootNode, childNode, edgeWeight = uvwTriplet
                graphMap[rootNode].append([childNode, edgeWeight])
                graphMap[childNode].append([rootNode, edgeWeight])

        def modArithmetic(xValue: int, yValue: int) -> int:
            return xValue - yValue * (xValue // yValue)

        populateGraph(edges, graph)

        n = len(graph)
        result = [0] * n

        def irregularDFS(alphaNode: int, betaParent: int, gammaDistance: int, deltaPath: List[int]) -> int:
            if modArithmetic(gammaDistance, signalSpeed) == 0:
                deltaPath.append(alphaNode)

            countAccum = 0
            for pair in graph[alphaNode]:
                neigh, wei = pair
                if neigh != betaParent:
                    countAccum += irregularDFS(neigh, betaParent, gammaDistance + wei, deltaPath)

            if modArithmetic(gammaDistance, signalSpeed) == 0:
                return countAccum + 1
            else:
                return countAccum

        def tallyPairsAround(centerNode: int) -> int:
            collectionOfPaths: List[List[int]] = []

            for pairEntry in graph[centerNode]:
                neighborAndWeight = pairEntry
                tempPath: List[int] = []
                irregularDFS(neighborAndWeight[0], centerNode, neighborAndWeight[1], tempPath)
                collectionOfPaths.append(tempPath)

            combinedPairs = 0
            xIndex = 0
            length = len(collectionOfPaths)
            while xIndex < length - 1:
                yIndex = xIndex + 1
                while yIndex < length:
                    combinedPairs += len(collectionOfPaths[xIndex]) * len(collectionOfPaths[yIndex])
                    yIndex += 1
                xIndex += 1

            return combinedPairs

        for loopVar in range(n):
            result[loopVar] = tallyPairsAround(loopVar)

        return result