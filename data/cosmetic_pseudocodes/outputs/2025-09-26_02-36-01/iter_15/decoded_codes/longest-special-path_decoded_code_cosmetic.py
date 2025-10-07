from typing import List, Tuple

class Solution:
    def longestSpecialPath(self, edges: List[Tuple[int, int, int]], nums: List[int]) -> List[int]:
        graph = [[] for _ in range(len(nums))]
        for alpha, beta, omega in edges:
            graph[alpha].append((beta, omega))
            graph[beta].append((alpha, omega))

        maxLength = 0
        minNodes = 1
        prefix = [0]
        lastSeenDepth = {}

        def dfs(delta: int, gamma: int, sigma: int, eta: int):
            nonlocal maxLength, minNodes
            priorDepth = lastSeenDepth.get(nums[delta], 0)
            lastSeenDepth[nums[delta]] = eta
            if sigma < priorDepth:
                sigma = priorDepth

            currentLength = prefix[-1] - prefix[sigma]
            currentNodes = eta - sigma
            if currentLength > maxLength or (currentLength == maxLength and currentNodes < minNodes):
                maxLength = currentLength
                minNodes = currentNodes

            for kappa, lam in graph[delta]:
                if kappa == gamma:
                    continue
                prefix.append(prefix[-1] + lam)
                dfs(kappa, delta, sigma, eta + 1)
                prefix.pop()

            lastSeenDepth[nums[delta]] = priorDepth

        dfs(0, -1, 0, 1)
        return [maxLength, minNodes]