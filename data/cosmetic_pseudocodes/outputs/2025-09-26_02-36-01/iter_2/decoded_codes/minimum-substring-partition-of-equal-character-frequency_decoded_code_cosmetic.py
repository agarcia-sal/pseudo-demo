from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def dfs(pos: int) -> int:
            if pos >= len(s):
                return 0

            charCount = defaultdict(int)
            countFreq = defaultdict(int)
            result = len(s) - pos

            idx = pos
            while idx < len(s):
                currentChar = s[idx]

                if charCount[currentChar] != 0:
                    oldFreq = charCount[currentChar]
                    countFreq[oldFreq] -= 1
                    if countFreq[oldFreq] == 0:
                        del countFreq[oldFreq]

                newFreq = charCount[currentChar] + 1
                charCount[currentChar] = newFreq
                countFreq[newFreq] += 1

                if len(countFreq) == 1:
                    tempResult = 1 + dfs(idx + 1)
                    if tempResult < result:
                        result = tempResult

                idx += 1

            return result

        return dfs(0)