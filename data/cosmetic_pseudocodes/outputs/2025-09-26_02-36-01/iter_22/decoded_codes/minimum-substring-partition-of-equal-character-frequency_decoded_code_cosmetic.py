from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def dfs(k: int) -> int:
            def incrementMap(mapping, key):
                mapping[key] += 1

            def decrementMap(mapping, key):
                if key in mapping:
                    mapping[key] -= 1
                    if mapping[key] == 0:
                        del mapping[key]

            if k >= len(s):
                return 0

            mapA = defaultdict(int)
            mapB = defaultdict(int)
            result = len(s) - k
            index = k

            while index < len(s):
                currentChar = s[index]

                if currentChar in mapA and mapA[currentChar] > 0:
                    decrementMap(mapB, mapA[currentChar])

                incrementMap(mapA, currentChar)
                incrementMap(mapB, mapA[currentChar])

                if len(mapB) == 1:
                    candidate = 1 + dfs(index + 1)
                    if candidate < result:
                        result = candidate

                index += 1

            return result

        return dfs(0)