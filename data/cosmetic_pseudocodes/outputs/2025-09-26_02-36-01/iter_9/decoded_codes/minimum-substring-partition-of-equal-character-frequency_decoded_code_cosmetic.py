from collections import defaultdict
from functools import lru_cache

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:

        def decrementFrequency(m, k):
            if k in m:
                m[k] -= 1
                if m[k] == 0:
                    del m[k]

        def incrementFrequency(m, k):
            m[k] = m.get(k, 0) + 1

        @lru_cache(None)
        def calculateMinimumPartitions(pos: int) -> int:
            if pos >= len(s):
                return 0

            charCounts = defaultdict(int)
            countFrequencies = defaultdict(int)
            minimumValue = len(s) - pos

            for loopIndex in range(pos, len(s)):
                currChar = s[loopIndex]

                if charCounts[currChar] != 0:
                    decrementFrequency(countFrequencies, charCounts[currChar])

                charCounts[currChar] += 1
                incrementFrequency(countFrequencies, charCounts[currChar])

                if len(countFrequencies) == 1:
                    candidate = 1 + calculateMinimumPartitions(loopIndex + 1)
                    if candidate < minimumValue:
                        minimumValue = candidate

            return minimumValue

        return calculateMinimumPartitions(0)