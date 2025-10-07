from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def dfs(currentIndex: int) -> int:
            if currentIndex >= len(s):
                return 0

            occurrenceMap = defaultdict(int)
            frequencyCounts = defaultdict(int)
            minimalCount = len(s) - currentIndex

            position = currentIndex
            while position < len(s):
                currentChar = s[position]

                if occurrenceMap[currentChar] != 0:
                    oldFreqValue = occurrenceMap[currentChar]
                    oldFreqCount = frequencyCounts[oldFreqValue]
                    frequencyCounts[oldFreqValue] = oldFreqCount - 1
                    if frequencyCounts[oldFreqValue] == 0:
                        del frequencyCounts[oldFreqValue]

                updatedCount = occurrenceMap[currentChar] + 1
                occurrenceMap[currentChar] = updatedCount

                frequencyCounts[updatedCount] += 1

                if len(frequencyCounts) == 1:
                    candidate = 1 + dfs(position + 1)
                    if candidate < minimalCount:
                        minimalCount = candidate

                position += 1

            return minimalCount

        return dfs(0)