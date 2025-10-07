from collections import defaultdict
from typing import List, Tuple

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        mapAlpha = defaultdict(list)
        mapBeta = defaultdict(list)

        def fillAdjacency(inputEdges: List[List[int]], adjacencyMap: defaultdict):
            for edge in inputEdges:
                elementX, elementY = edge[0], edge[1]
                if elementX not in adjacencyMap:
                    adjacencyMap[elementX] = []
                if elementY not in adjacencyMap:
                    adjacencyMap[elementY] = []
                adjacencyMap[elementX].append(elementY)
                adjacencyMap[elementY].append(elementX)

        fillAdjacency(edges1, mapAlpha)
        fillAdjacency(edges2, mapBeta)

        sizeAlpha = len(mapAlpha)
        sizeBeta = len(mapBeta)

        def traverse(treeStructure: dict, rootNode: int) -> Tuple[int, int]:
            countEven = 0
            countOdd = 0
            dequeStorage = [(rootNode, 0)]
            discovered = {rootNode}

            def processQueue(queueList: List[Tuple[int, int]], discoveredSet: set, evenCnt: int, oddCnt: int) -> Tuple[int, int]:
                if not queueList:
                    return evenCnt, oddCnt

                currentPair = queueList[0]
                newQueue = queueList[1:]
                currentNode, currentDistance = currentPair

                if currentDistance % 2 == 0:
                    updatedEven = evenCnt + 1
                    updatedOdd = oddCnt
                else:
                    updatedEven = evenCnt
                    updatedOdd = oddCnt + 1

                neighborsList = treeStructure[currentNode]
                indexNeighbor = len(neighborsList) - 1

                while indexNeighbor >= 0:
                    neighborElem = neighborsList[indexNeighbor]
                    if neighborElem not in discoveredSet:
                        discoveredSet.add(neighborElem)
                        newQueue.append((neighborElem, currentDistance + 1))
                    indexNeighbor -= 1

                return processQueue(newQueue, discoveredSet, updatedEven, updatedOdd)

            return processQueue(dequeStorage, discovered, countEven, countOdd)

        listCountsAlpha = []
        for idxAlpha in range(sizeAlpha):
            countsAlpha = traverse(mapAlpha, idxAlpha)
            listCountsAlpha.append(countsAlpha)

        listCountsBeta = []
        for idxBeta in range(sizeBeta):
            countsBeta = traverse(mapBeta, idxBeta)
            listCountsBeta.append(countsBeta)

        finalResults = []
        for posAlpha in range(sizeAlpha):
            valEvenAlpha, valOddAlpha = listCountsAlpha[posAlpha]
            maximumTarget = 0
            for posBeta in range(sizeBeta):
                valEvenBeta, valOddBeta = listCountsBeta[posBeta]
                if posAlpha == posBeta or (posAlpha % 2) == (posBeta % 2):
                    candidateCount = valEvenBeta
                else:
                    candidateCount = valOddBeta
                if candidateCount > maximumTarget:
                    maximumTarget = candidateCount
            sumResult = valEvenAlpha + maximumTarget
            finalResults.append(sumResult)

        return finalResults