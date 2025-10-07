import heapq
from collections import defaultdict
from math import inf
from typing import List, Tuple

class Solution:
    def findAnswer(self, n: int, edges: List[Tuple[int, int, int]]) -> List[bool]:
        adjacencyMap = defaultdict(list)
        idx = 0
        while idx < len(edges):
            uNode, vNode, wWeight = edges[idx]
            adjacencyMap[uNode].append((vNode, wWeight))
            adjacencyMap[vNode].append((uNode, wWeight))
            idx += 1

        distanceList = [inf] * n
        distanceList[0] = 0
        heapQueue = [(0, 0)]

        while heapQueue:
            currentDistance, currentNode = heapq.heappop(heapQueue)
            if currentDistance > distanceList[currentNode]:
                continue
            nbrIndex = 0
            while nbrIndex < len(adjacencyMap[currentNode]):
                adjNode, adjWeight = adjacencyMap[currentNode][nbrIndex]
                calculatedDist = currentDistance + adjWeight
                if calculatedDist < distanceList[adjNode]:
                    distanceList[adjNode] = calculatedDist
                    heapq.heappush(heapQueue, (calculatedDist, adjNode))
                nbrIndex += 1

        edgesInShortestPath = set()
        nodeStack = [(n - 1, distanceList[n - 1])]
        visitedFlags = [False] * n

        while nodeStack:
            currentNode, currentDist = nodeStack.pop()
            if visitedFlags[currentNode]:
                continue
            visitedFlags[currentNode] = True
            adjIndex = 0
            while adjIndex < len(adjacencyMap[currentNode]):
                neighborNode, weightVal = adjacencyMap[currentNode][adjIndex]
                if currentDist == distanceList[neighborNode] + weightVal:
                    minNode, maxNode = (currentNode, neighborNode) if currentNode < neighborNode else (neighborNode, currentNode)
                    edgesInShortestPath.add((minNode, maxNode))
                    nodeStack.append((neighborNode, distanceList[neighborNode]))
                adjIndex += 1

        resultArray = []
        edgeIndex = 0
        while edgeIndex < len(edges):
            firstNode, secondNode, _ = edges[edgeIndex]
            minVal, maxVal = (firstNode, secondNode) if firstNode < secondNode else (secondNode, firstNode)
            resultArray.append((minVal, maxVal) in edgesInShortestPath)
            edgeIndex += 1

        return resultArray