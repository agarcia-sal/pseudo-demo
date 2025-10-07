from typing import List, Tuple, Dict

class Solution:
    def longestSpecialPath(self, edges: List[Tuple[int, int, int]], nums: List[int]) -> List[int]:
        n = len(nums)
        adjacency: List[List[Tuple[int, int]]] = [[] for _ in range(n)]

        for a, b, c in edges:
            adjacency[a].append((b, c))
            adjacency[b].append((a, c))

        maxLength = 0
        minNodes = 1
        prefix = [0]
        lastSeenDepth: Dict[int, int] = {}

        def dfs(vertex: int, parent: int, boundary: int, depth: int):
            nonlocal maxLength, minNodes
            previousDepth = lastSeenDepth.get(nums[vertex], 0)
            lastSeenDepth[nums[vertex]] = depth

            if boundary < previousDepth:
                boundary = previousDepth

            pathLen = prefix[-1] - prefix[boundary]
            nodeCount = depth - boundary

            if pathLen > maxLength:
                maxLength = pathLen
                minNodes = nodeCount
            elif pathLen == maxLength and nodeCount < minNodes:
                minNodes = nodeCount

            for neighbor, weight in adjacency[vertex]:
                if neighbor == parent:
                    continue
                prefix.append(prefix[-1] + weight)
                dfs(neighbor, vertex, boundary, depth + 1)
                prefix.pop()

            lastSeenDepth[nums[vertex]] = previousDepth

        dfs(0, -1, 0, 1)
        return [maxLength, minNodes]