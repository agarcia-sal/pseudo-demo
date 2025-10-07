from math import inf
from typing import List, Tuple

class Solution:
    def shortestDistanceAfterQueries(self, length: int, requestList: List[Tuple[int, int]]) -> List[int]:
        adjacencyMap = {x: [] for x in range(length)}

        def buildEdges(index: int) -> None:
            if index >= length - 1:
                return
            nextNode = index + 1
            edgeTuple = (nextNode, 1)
            adjacencyMap[index].append(edgeTuple)
            buildEdges(index + 1)

        buildEdges(0)

        def dijkstra() -> int:
            distances = [inf] * length
            distances[0] = 0
            priorityQueue: List[Tuple[int, int]] = [(0, 0)]

            def heapPopLowest(pq: List[Tuple[int, int]]) -> Tuple[int, int] or None:
                if len(pq) == 0:
                    return None
                minIndex = 0
                for idx in range(1, len(pq)):
                    if pq[idx][0] < pq[minIndex][0]:
                        minIndex = idx
                poppedElement = pq[minIndex]
                # Remove by swapping with last element for O(1) pop or direct removal
                pq[minIndex] = pq[-1]
                pq.pop()
                return poppedElement

            def heapPushMaintainHeap(pq: List[Tuple[int, int]], entry: Tuple[int, int]) -> None:
                pq.append(entry)

            def processQueue() -> None:
                extraction = heapPopLowest(priorityQueue)
                if extraction is None:
                    return
                currentDistance, currentVertex = extraction
                if currentDistance > distances[currentVertex]:
                    processQueue()
                    return

                def iterateNeighbors(index: int) -> None:
                    if index == len(adjacencyMap[currentVertex]):
                        processQueue()
                        return
                    adjacentNode, edgeWeight = adjacencyMap[currentVertex][index]
                    newDistance = currentDistance + edgeWeight
                    if newDistance < distances[adjacentNode]:
                        distances[adjacentNode] = newDistance
                        heapPushMaintainHeap(priorityQueue, (newDistance, adjacentNode))
                    iterateNeighbors(index + 1)

                iterateNeighbors(0)

            processQueue()
            return distances[length - 1]

        outputResults = []

        def processQueries(qIndex: int) -> None:
            if qIndex == len(requestList):
                return
            startNode, edgeVal = requestList[qIndex]
            adjacencyMap[startNode].append((edgeVal, 1))
            dijkstraResult = dijkstra()
            outputResults.append(dijkstraResult)
            processQueries(qIndex + 1)

        processQueries(0)
        return outputResults