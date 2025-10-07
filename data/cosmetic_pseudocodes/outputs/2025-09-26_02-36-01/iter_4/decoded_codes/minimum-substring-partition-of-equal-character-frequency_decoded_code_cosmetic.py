from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def dfs(index: int) -> int:
            if index >= len(s):
                return 0
            charCount = defaultdict(int)
            frequencyMap = defaultdict(int)
            minimumPartitions = len(s) - index
            currentPos = index
            while currentPos < len(s):
                currentChar = s[currentPos]
                oldCount = charCount[currentChar]
                if oldCount != 0:
                    frequencyMap[oldCount] -= 1
                    if frequencyMap[oldCount] == 0:
                        del frequencyMap[oldCount]
                newCount = oldCount + 1
                charCount[currentChar] = newCount
                frequencyMap[newCount] += 1
                if len(frequencyMap) == 1:
                    candidatePartitions = 1 + dfs(currentPos + 1)
                    if candidatePartitions < minimumPartitions:
                        minimumPartitions = candidatePartitions
                currentPos += 1
            return minimumPartitions

        return dfs(0)