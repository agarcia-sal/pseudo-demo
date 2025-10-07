from typing import List, Tuple, Dict

class Solution:
    def longestSpecialPath(self, edges: List[Tuple[int, int, int]], nums: List[int]) -> List[int]:
        n = len(nums)
        adjacencyLists: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        for a, b, c in edges:
            adjacencyLists[a].append((b, c))
            adjacencyLists[b].append((a, c))

        maxLength = 0
        minNodes = 1
        prefix = [0]
        lastSeenDepth: Dict[int, int] = {}

        def traverse(x: int, prevNode: int, boundaryIndex: int, depthCount: int) -> None:
            nonlocal maxLength, minNodes
            savedDepth = lastSeenDepth.get(nums[x], 0)
            lastSeenDepth[nums[x]] = depthCount

            if boundaryIndex < savedDepth:
                boundaryIndex = savedDepth

            segmentLength = prefix[-1] - prefix[boundaryIndex]
            nodeDiff = depthCount - boundaryIndex

            if segmentLength > maxLength or (segmentLength == maxLength and nodeDiff < minNodes):
                maxLength = segmentLength
                minNodes = nodeDiff

            for neighbor, weightVal in adjacencyLists[x]:
                if neighbor == prevNode:
                    continue
                prefix.append(prefix[-1] + weightVal)
                traverse(neighbor, x, boundaryIndex, depthCount + 1)
                prefix.pop()

            lastSeenDepth[nums[x]] = savedDepth

        traverse(0, -1, 0, 1)
        return [maxLength, minNodes]