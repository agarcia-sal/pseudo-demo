from typing import List, Dict, Tuple

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        # Build adjacency list A: for each node, a list of (neighbor, weight)
        A: List[List[Tuple[int, int]]] = [[] for _ in range(len(nums))]

        for edge in edges:
            u, v, w = edge
            A[u].append((v, w))
            A[v].append((u, w))

        maxLength = 0
        minNodes = 1
        prefix = [0]  # Prefix sums of weights along the current path
        lastSeenDepth: Dict[int, int] = {}  # Maps nums[node] to the depth in path

        def dfs(H: int, I: int, J: int, K: int):
            nonlocal maxLength, minNodes, prefix, lastSeenDepth

            L = lastSeenDepth.get(nums[H], 0)

            lastSeenDepth[nums[H]] = K
            if J < L:
                J = L

            M = prefix[-1] - prefix[J]
            N = K - J

            if (M > maxLength) or (M == maxLength and N < minNodes):
                maxLength = M
                minNodes = N

            for (P, Q) in A[H]:
                if P != I:
                    prefix.append(prefix[-1] + Q)
                    dfs(P, H, J, K + 1)
                    prefix.pop()

            lastSeenDepth[nums[H]] = L

        dfs(0, -1, 0, 1)

        return [maxLength, minNodes]