from collections import defaultdict
from typing import List, Tuple


class Solution:
    def countPairsOfConnectableServers(self, edges: List[Tuple[int, int, int]], signalSpeed: int) -> List[int]:
        adjacency = defaultdict(list)
        for nodeA, nodeB, edgeWeight in edges:
            adjacency[nodeA].append((nodeB, edgeWeight))
            adjacency[nodeB].append((nodeA, edgeWeight))

        nodeCount = len(adjacency)
        answerArray = [0] * nodeCount

        def traverseGraph(currentVertex: int, cameFrom: int, accumulatedDist: int, visitedNodes: List[int]) -> int:
            if accumulatedDist % signalSpeed == 0:
                visitedNodes.append(currentVertex)
            subtotal = 0
            for connectedVertex, edgeLen in adjacency[currentVertex]:
                if connectedVertex != cameFrom:
                    subtotal += traverseGraph(connectedVertex, currentVertex, accumulatedDist + edgeLen, visitedNodes)
            return subtotal + (1 if accumulatedDist % signalSpeed == 0 else 0)

        def pairsViaCenter(centerNode: int) -> int:
            collectedPaths = []
            for nextNode, edgeValue in adjacency[centerNode]:
                tempPath = []
                traverseGraph(nextNode, centerNode, edgeValue, tempPath)
                collectedPaths.append(tempPath)

            combinedPairs = 0
            length = len(collectedPaths)
            for iIndex in range(length - 1):
                len_i = len(collectedPaths[iIndex])
                for jIndex in range(iIndex + 1, length):
                    len_j = len(collectedPaths[jIndex])
                    combinedPairs += len_i * len_j
            return combinedPairs

        for nodeIterator in range(nodeCount):
            answerArray[nodeIterator] = pairsViaCenter(nodeIterator)

        return answerArray