from collections import defaultdict
from typing import List, Tuple

class Solution:
    def longestSpecialPath(self, edges: List[Tuple[int, int, int]], nums: List[int]) -> List[int]:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        maxLength = 0
        minNodes = 1
        prefix = [0]
        lastSeenDepth = dict()

        def dfs(current: int, parent: int, leftBound: int, depth: int) -> None:
            nonlocal maxLength, minNodes
            prevDepth = lastSeenDepth.get(nums[current], 0)
            lastSeenDepth[nums[current]] = depth

            if leftBound < prevDepth:
                leftBound = prevDepth

            pathLength = prefix[-1] - prefix[leftBound]
            pathNodes = depth - leftBound

            if pathLength > maxLength or (pathLength == maxLength and pathNodes < minNodes):
                maxLength = pathLength
                minNodes = pathNodes

            for neighbor, weight in graph[current]:
                if neighbor != parent:
                    prefix.append(prefix[-1] + weight)
                    dfs(neighbor, current, leftBound, depth + 1)
                    prefix.pop()

            lastSeenDepth[nums[current]] = prevDepth

        dfs(0, -1, 0, 1)

        return [maxLength, minNodes]