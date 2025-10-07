from collections import defaultdict
from typing import List, Tuple

class Solution:
    def longestSpecialPath(self, edges: List[Tuple[int, int, int]], nums: List[int]) -> List[int]:
        n = len(nums)
        adjacency = [[] for _ in range(n)]
        for nodeA, nodeB, edgeWeight in edges:
            adjacency[nodeA].append((nodeB, edgeWeight))
            adjacency[nodeB].append((nodeA, edgeWeight))

        maxLength = 0
        minNodes = 1
        prefix = [0]
        lastSeenDepth = dict()

        def dfs(currentNode: int, lastNode: int, boundaryIndex: int, depthCount: int):
            nonlocal maxLength, minNodes
            previousDepth = lastSeenDepth.get(nums[currentNode], 0)
            lastSeenDepth[nums[currentNode]] = depthCount

            if boundaryIndex < previousDepth:
                boundaryIndex = previousDepth

            segmentLength = prefix[-1] - prefix[boundaryIndex]
            segmentNodes = depthCount - boundaryIndex

            if segmentLength > maxLength:
                maxLength = segmentLength
                minNodes = segmentNodes
            elif segmentLength == maxLength and segmentNodes < minNodes:
                minNodes = segmentNodes

            for neighbor, edgeValue in adjacency[currentNode]:
                if neighbor != lastNode:
                    currentSum = prefix[-1] + edgeValue
                    prefix.append(currentSum)
                    dfs(neighbor, currentNode, boundaryIndex, depthCount + 1)
                    prefix.pop()

            lastSeenDepth[nums[currentNode]] = previousDepth

        dfs(0, -1, 0, 1)
        return [maxLength, minNodes]