from typing import List, Tuple

class Solution:
    def longestSpecialPath(self, edges: List[Tuple[int, int, int]], nums: List[int]) -> List[int]:
        adjacency = [[] for _ in range(len(nums))]
        for a, b, c in edges:
            adjacency[a].append((b, c))
            adjacency[b].append((a, c))

        maxLength = 0
        minNodes = 1
        prefix = [0]
        lastSeenDepth = {}

        def dfs(curr: int, prevNode: int, boundary: int, depth: int) -> None:
            nonlocal maxLength, minNodes
            originalDepth = lastSeenDepth.get(nums[curr], 0)
            lastSeenDepth[nums[curr]] = depth

            if boundary < originalDepth:
                boundary = originalDepth

            segmentLength = prefix[-1] - prefix[boundary]
            segmentNodes = depth - boundary

            if segmentLength > maxLength or (segmentLength == maxLength and segmentNodes < minNodes):
                maxLength = segmentLength
                minNodes = segmentNodes

            for neighbor, weight in adjacency[curr]:
                if neighbor == prevNode:
                    continue
                prefix.append(prefix[-1] + weight)
                dfs(neighbor, curr, boundary, depth + 1)
                prefix.pop()

            lastSeenDepth[nums[curr]] = originalDepth

        dfs(0, -1, 0, 1)
        return [maxLength, minNodes]