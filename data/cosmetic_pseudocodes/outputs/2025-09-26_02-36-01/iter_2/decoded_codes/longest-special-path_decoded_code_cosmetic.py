from typing import List, Tuple


class Solution:
    def longestSpecialPath(self, edges: List[Tuple[int, int, int]], nums: List[int]) -> List[int]:
        adjacency = [[] for _ in range(len(nums))]

        for a, b, c in edges:
            adjacency[a].append((b, c))
            adjacency[b].append((a, c))

        maxLen = 0
        minCount = 1
        prefix = [0]
        lastSeenDepth = {}

        def dfs(node: int, parent: int, leftLim: int, depth: int):
            nonlocal maxLen, minCount
            prevDepthSeen = lastSeenDepth.get(nums[node], 0)
            lastSeenDepth[nums[node]] = depth

            if leftLim < prevDepthSeen:
                leftLim = prevDepthSeen

            currentLength = prefix[-1] - prefix[leftLim]
            nodeCount = depth - leftLim
            if currentLength > maxLen or (currentLength == maxLen and nodeCount < minCount):
                maxLen = currentLength
                minCount = nodeCount

            for adjNode, weight in adjacency[node]:
                if adjNode == parent:
                    continue
                prefix.append(prefix[-1] + weight)
                dfs(adjNode, node, leftLim, depth + 1)
                prefix.pop()

            lastSeenDepth[nums[node]] = prevDepthSeen

        dfs(0, -1, 0, 1)
        return [maxLen, minCount]