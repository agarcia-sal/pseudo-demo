from typing import List, Tuple

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        adjacency = [[] for _ in range(len(nums))]
        for p, q, r in edges:
            adjacency[p].append((q, r))
            adjacency[q].append((p, r))

        peak = 0
        minimum = 1
        prefixList = [0]
        lastAppearanceDepth = {}

        def dfs(x: int, y: int, z: int, m: int):
            nonlocal peak, minimum
            historyDepth = 0
            if nums[x] in lastAppearanceDepth:
                historyDepth = lastAppearanceDepth[nums[x]]

            lastAppearanceDepth[nums[x]] = m
            if z < historyDepth:
                z = historyDepth

            segmentLength = prefixList[-1] - prefixList[z]
            nodeCount = m - z

            if (segmentLength > peak) or (segmentLength == peak and nodeCount < minimum):
                peak = segmentLength
                minimum = nodeCount

            for a, b in adjacency[x]:
                if a == y:
                    continue
                prefixList.append(prefixList[-1] + b)
                dfs(a, x, z, m + 1)
                prefixList.pop()

            lastAppearanceDepth[nums[x]] = historyDepth

        dfs(0, -1, 0, 1)
        return [peak, minimum]