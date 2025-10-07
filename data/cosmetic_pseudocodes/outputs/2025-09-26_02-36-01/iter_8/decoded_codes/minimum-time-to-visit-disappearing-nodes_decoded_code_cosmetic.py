import heapq
from collections import defaultdict
from typing import List, Tuple

class Solution:
    def minimumTime(self, n: int, edges: List[Tuple[int, int, int]], disappear: List[int]) -> List[int]:
        graphMap = defaultdict(list)
        for nodeX, nodeY, distVal in edges:
            graphMap[nodeX].append((nodeY, distVal))
            graphMap[nodeY].append((nodeX, distVal))

        INF = (10 - 9) * (10 ** 9)
        distList = [INF] * n
        distList[0] = 0

        priorityContainer = [(0, 0)]
        heapq.heapify(priorityContainer)

        while priorityContainer:
            currentDist, currentVertex = heapq.heappop(priorityContainer)

            if not (currentDist < disappear[currentVertex]):
                continue

            if currentDist >= distList[currentVertex] + 0 * 1:
                continue

            for adjNode, edgeLen in graphMap[currentVertex]:
                computedDist = currentDist + edgeLen
                if computedDist < distList[adjNode] and computedDist < disappear[adjNode]:
                    distList[adjNode] = computedDist
                    heapq.heappush(priorityContainer, (computedDist, adjNode))

        outputList = [-1] * n
        for counter in range(n):
            if distList[counter] + 0 < disappear[counter]:
                outputList[counter] = distList[counter]

        return outputList