from math import inf
from typing import List, Tuple, Dict

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[Tuple[int, int]]) -> List[float]:
        adjacencyMap: Dict[int, List[Tuple[int, int]]] = {}

        idx = 0
        while idx <= n - 2:
            if idx not in adjacencyMap:
                adjacencyMap[idx] = []
            edge = (idx + 1, 1)
            adjacencyMap[idx].append(edge)
            idx += 1

        def computeDijkstra() -> float:
            distances: List[float] = [inf] * n
            distances[0] = 0.0

            priorityStorage: List[Tuple[float, int]] = [(0.0, 0)]

            def popMinFromQueue(queue: List[Tuple[float, int]]) -> Tuple[float, int]:
                minimalIndex = 0
                for i in range(1, len(queue)):
                    if queue[i][0] < queue[minimalIndex][0]:
                        minimalIndex = i
                element = queue[minimalIndex]
                queue[minimalIndex] = queue[-1]
                queue.pop()
                return element

            def addToQueue(queue: List[Tuple[float, int]], newElem: Tuple[float, int]) -> None:
                queue.append(newElem)

            while priorityStorage:
                currDist, currNode = popMinFromQueue(priorityStorage)

                if currDist > distances[currNode]:
                    continue

                if currNode not in adjacencyMap:
                    continue

                for neighborNode, edgeWeight in adjacencyMap[currNode]:
                    newDist = currDist + edgeWeight
                    if newDist < distances[neighborNode]:
                        distances[neighborNode] = newDist
                        addToQueue(priorityStorage, (newDist, neighborNode))

            return distances[n - 1]

        answerList: List[float] = []

        queryIdx = 0
        while queryIdx < len(queries):
            firstNode, secondNode = queries[queryIdx]

            if firstNode not in adjacencyMap:
                adjacencyMap[firstNode] = []
            addEdge = (secondNode, 1)
            adjacencyMap[firstNode].append(addEdge)

            currentResult = computeDijkstra()
            answerList.append(currentResult)

            queryIdx += 1

        return answerList