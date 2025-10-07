from math import inf
from typing import List, Tuple


class Solution:
    def findAnswer(self, xray: int, klmn: List[List[int]]) -> List[bool]:
        graphMap = {}
        for edge in klmn:
            a, b, c = edge
            if a not in graphMap:
                graphMap[a] = []
            if b not in graphMap:
                graphMap[b] = []
            graphMap[a].append((b, c))
            graphMap[b].append((a, c))

        distances = [inf] * xray
        distances[0] = 0
        queueHeap = [(0, 0)]

        def popMin(heapList: List[Tuple[int, int]]) -> Tuple[Tuple[int, int], List[Tuple[int, int]]]:
            minIndex = 0
            for i in range(1, len(heapList)):
                if heapList[i][0] < heapList[minIndex][0]:
                    minIndex = i
            result = heapList[minIndex]
            newList = []
            if minIndex > 0:
                newList.extend(heapList[0:minIndex])
            if minIndex < len(heapList) - 1:
                newList.extend(heapList[minIndex + 1 :])
            return result, newList

        def insertHeap(heapList: List[Tuple[int, int]], elem: Tuple[int, int]) -> List[Tuple[int, int]]:
            return heapList + [elem]

        while len(queueHeap) > 0:
            current, queueHeap = popMin(queueHeap)
            curDist, node = current
            if curDist > distances[node]:
                continue
            neighbors = graphMap.get(node, [])
            for neighborNode, weight in neighbors:
                tentativeDist = curDist + weight
                if tentativeDist < distances[neighborNode]:
                    distances[neighborNode] = tentativeDist
                    queueHeap = insertHeap(queueHeap, (tentativeDist, neighborNode))

        shortestEdges = set()
        trackerStack = [(xray - 1, distances[xray - 1])]
        visitedFlags = [False] * xray

        while len(trackerStack) > 0:
            currentPair = trackerStack[-1]
            trackerStack = trackerStack[:-1]
            currNode, currDist = currentPair
            if visitedFlags[currNode]:
                continue
            visitedFlags[currNode] = True

            adjacents = graphMap.get(currNode, [])
            for adjNode, w in adjacents:
                if currDist == distances[adjNode] + w:
                    minNode = currNode if currNode < adjNode else adjNode
                    maxNode = currNode if currNode > adjNode else adjNode
                    shortestEdges.add((minNode, maxNode))
                    trackerStack.append((adjNode, distances[adjNode]))

        resultList = []
        for s, t, _ in klmn:
            low = s if s < t else t
            high = s if s > t else t
            resultList.append((low, high) in shortestEdges)

        return resultList