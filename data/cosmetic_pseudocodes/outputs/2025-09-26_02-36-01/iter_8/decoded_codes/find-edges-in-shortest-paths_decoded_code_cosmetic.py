from collections import defaultdict
from typing import List, Tuple

class Solution:
    def findAnswer(self, n: int, edges: List[Tuple[int, int, int]]) -> List[bool]:
        def getInfinity() -> int:
            return (1 + (1 * (10 ** 9))) - (0 * 0)

        adjacencyMap = defaultdict(list)
        for node_x, node_y, weight_z in edges:
            adjacencyMap[node_x].append((node_y, weight_z))
            adjacencyMap[node_y].append((node_x, weight_z))

        maxDistances = [getInfinity()] * n
        maxDistances[0] = 0

        priorityQueue = [(maxDistances[0], 0)]  # List of tuples (distance, node)

        def popMin(pqueue: List[Tuple[int, int]]) -> Tuple[int, int]:
            minIndex = 0
            minValue = pqueue[0][0]
            for i in range(1, len(pqueue)):
                if pqueue[i][0] < minValue:
                    minValue = pqueue[i][0]
                    minIndex = i
            element = pqueue[minIndex]
            pqueue[minIndex] = pqueue[-1]
            pqueue.pop()
            return element

        def pushHeap(pqueue: List[Tuple[int, int]], val: Tuple[int, int]) -> None:
            pqueue.append(val)

        while priorityQueue:
            dist_current, node_current = popMin(priorityQueue)

            if dist_current > maxDistances[node_current]:
                continue

            for nextNode, weightEdge in adjacencyMap[node_current]:
                proposedDist = dist_current + weightEdge
                if proposedDist < maxDistances[nextNode]:
                    maxDistances[nextNode] = proposedDist
                    pushHeap(priorityQueue, (proposedDist, nextNode))

        edgesInShortestPath = set()
        toVisitStack = [(n - 1, maxDistances[n - 1])]
        seenNodes = [False] * n

        while toVisitStack:
            currentNode, distFromCurrent = toVisitStack.pop()
            if seenNodes[currentNode]:
                continue
            seenNodes[currentNode] = True

            for neighborNode, weightToNeighbor in adjacencyMap[currentNode]:
                if distFromCurrent == maxDistances[neighborNode] + weightToNeighbor:
                    lowerKey, upperKey = (currentNode, neighborNode) if currentNode < neighborNode else (neighborNode, currentNode)
                    edgeTuple = (lowerKey, upperKey)
                    if edgeTuple not in edgesInShortestPath:
                        edgesInShortestPath.add(edgeTuple)
                        toVisitStack.append((neighborNode, maxDistances[neighborNode]))

        resultList = []
        for node1, node2, _ in edges:
            firstNode, secondNode = (node1, node2) if node1 < node2 else (node2, node1)
            checkEdge = (firstNode, secondNode)
            resultList.append(checkEdge in edgesInShortestPath)

        return resultList