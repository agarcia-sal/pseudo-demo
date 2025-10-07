from typing import List, Tuple

class Solution:
    def longestSpecialPath(self, edges: List['Edge'], nums: List[int]) -> List[int]:
        adjacency = [[] for _ in range(len(nums))]
        for edge in edges:
            adjacency[edge.u].append((edge.v, edge.w))
            adjacency[edge.v].append((edge.u, edge.w))

        maxLength = 0
        minNodes = 1
        prefix = [0]
        lastSeenDepth = {}

        def dfs(currentNode: int, previousNode: int, boundary: int, depth: int):
            nonlocal maxLength, minNodes

            priorDepth = lastSeenDepth.get(nums[currentNode], 0)
            lastSeenDepth[nums[currentNode]] = depth
            if boundary < priorDepth:
                boundary = priorDepth

            pathSum = prefix[-1] - prefix[boundary]
            pathNodes = depth - boundary

            if pathSum > maxLength or (pathSum == maxLength and pathNodes < minNodes):
                maxLength = pathSum
                minNodes = pathNodes

            for nextNode, weightVal in adjacency[currentNode]:
                if nextNode == previousNode:
                    continue
                prefix.append(prefix[-1] + weightVal)
                dfs(nextNode, currentNode, boundary, depth + 1)
                prefix.pop()

            lastSeenDepth[nums[currentNode]] = priorDepth

        dfs(0, -1, 0, 1)
        return [maxLength, minNodes]

# Supporting Edge class to match pseudocode structure
class Edge:
    def __init__(self, u: int, v: int, w: int):
        self.u = u
        self.v = v
        self.w = w