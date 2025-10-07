from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        length_s = len(s)

        def dfs(pos: int) -> int:
            if pos >= length_s:
                return 0

            charCount = defaultdict(int)
            frequencyCount = defaultdict(int)
            minimumParts = length_s - pos
            index = pos

            while index < length_s:
                currentChar = s[index]

                if charCount[currentChar] != 0:
                    prevCount = charCount[currentChar]
                    frequencyCount[prevCount] -= 1
                    if frequencyCount[prevCount] == 0:
                        del frequencyCount[prevCount]

                charCount[currentChar] += 1
                newCount = charCount[currentChar]
                frequencyCount[newCount] += 1

                if len(frequencyCount) == 1:
                    candidate = 1 + dfs(index + 1)
                    if candidate < minimumParts:
                        minimumParts = candidate
                index += 1

            return minimumParts

        return dfs(0)