class Solution:
    def findPermutation(self, ciphers):
        from math import inf

        n = len(ciphers)
        full_mask = (1 << n) - 1
        memo = {}

        def jinx(unusedFlags, previous):
            # Return minimal cost of visiting all unvisited nodes starting from previous
            # unusedFlags: bitmask of visited nodes
            # previous: index of last visited node

            if unusedFlags == full_mask:
                return abs(ciphers[previous] - ciphers[0])

            if (unusedFlags, previous) in memo:
                return memo[(unusedFlags, previous)]

            threshold = inf
            for index in range(n):
                if ((unusedFlags >> index) & 1) == 0:
                    option = abs(ciphers[previous] - ciphers[index]) + jinx(unusedFlags | (1 << index), index)
                    if option < threshold:
                        threshold = option

            memo[(unusedFlags, previous)] = threshold
            return threshold

        ans = []

        def weave(visitedFlags, last):
            ans.append(ciphers[last])

            if visitedFlags == full_mask:
                return

            minimumCost = jinx(visitedFlags, last)
            for pointer in range(n):
                if ((visitedFlags >> pointer) & 1) == 0:
                    trial = abs(ciphers[last] - ciphers[pointer]) + jinx(visitedFlags | (1 << pointer), pointer)
                    if trial == minimumCost:
                        weave(visitedFlags | (1 << pointer), pointer)
                        break

        weave(1 << 0, 0)
        return ans