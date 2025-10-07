from collections import defaultdict
from functools import lru_cache

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        @lru_cache(None)
        def dfs(index: int) -> int:
            if index >= len(s):
                return 0

            countMap = defaultdict(int)
            freqMap = defaultdict(int)
            result = len(s) - index

            for pos in range(index, len(s)):
                char = s[pos]

                if countMap[char] > 0:
                    frequency = countMap[char]
                    freqMap[frequency] -= 1
                    if freqMap[frequency] == 0:
                        del freqMap[frequency]

                countMap[char] += 1
                freqMap[countMap[char]] += 1

                if len(freqMap) == 1:
                    temp = 1 + dfs(pos + 1)
                    if temp < result:
                        result = temp

            return result

        return dfs(0)