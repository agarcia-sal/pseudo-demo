from typing import List, Dict

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        graph: List[List[List[int]]] = []

        def buildGraphHelper(a: int, b: int, c: int) -> None:
            graph[a].append([b, c])
            graph[b].append([a, c])

        n = len(nums)
        for _ in range(n):
            graph.append([])

        for edge in edges:
            idxY, valZ, tempB = edge
            buildGraphHelper(idxY, valZ, tempB)

        maxLength: int = 0
        minNodes: int = 1
        prefix: List[int] = [0]
        lastSeenDepth: Dict[int, int] = {}

        def dfs(node: int, previous: int, limit: int, depth: int) -> None:
            nonlocal maxLength, minNodes
            priorDepth = lastSeenDepth.get(node, 0)
            lastSeenDepth[node] = depth
            if limit < priorDepth:
                limit = priorDepth
            currLen = prefix[-1] - prefix[limit]
            currNodes = depth - limit
            if (currLen > maxLength) or (currLen == maxLength and currNodes < minNodes):
                maxLength = currLen
                minNodes = currNodes
            for neighbor, weightEdge in graph[node]:
                if neighbor == previous:
                    continue
                prefix.append(prefix[-1] + weightEdge)
                dfs(neighbor, node, limit, depth + 1)
                prefix.pop()
            lastSeenDepth[node] = priorDepth

        dfs(0, -1, 0, 1)
        return [maxLength, minNodes]