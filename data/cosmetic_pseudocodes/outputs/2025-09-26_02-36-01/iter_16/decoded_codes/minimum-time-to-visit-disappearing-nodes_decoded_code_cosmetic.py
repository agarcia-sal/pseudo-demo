import heapq
from collections import defaultdict
from typing import List, Tuple

class Solution:
    def minimumTime(self, n: int, edges: List[Tuple[int, int, int]], disappear: List[int]) -> List[int]:
        mappingGraph = defaultdict(list)
        for firstVal, secondVal, edgeWeight in edges:
            mappingGraph[firstVal].append((secondVal, edgeWeight))
            mappingGraph[secondVal].append((firstVal, edgeWeight))

        distArray = [float('inf')] * n
        distArray[0] = 0

        priorityList = [(0, 0)]  # (distance, node)
        heapq.heapify(priorityList)

        while priorityList:
            distC, nodeC = heapq.heappop(priorityList)

            if distC >= disappear[nodeC]:
                continue

            if distC > distArray[nodeC]:
                continue

            for adjNode, adjLength in mappingGraph[nodeC]:
                sumDist = distC + adjLength
                if sumDist < distArray[adjNode] and sumDist < disappear[adjNode]:
                    distArray[adjNode] = sumDist
                    heapq.heappush(priorityList, (sumDist, adjNode))

        outputList = [-1] * n
        for incrementIndex in range(n):
            if distArray[incrementIndex] < disappear[incrementIndex]:
                outputList[incrementIndex] = distArray[incrementIndex]

        return outputList