from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        def hasCharAtLeastK(freqMap, threshold):
            # Check if any character frequency is at least threshold
            for count in freqMap.values():
                if count >= threshold:
                    return True
            return False

        freqCounts = defaultdict(int)
        resultSum = 0
        leftIndex = 0

        def processRight(rIndex):
            nonlocal leftIndex, resultSum
            if rIndex == len(s):
                return
            currentChar = s[rIndex]
            freqCounts[currentChar] += 1

            while hasCharAtLeastK(freqCounts, k):
                leftChar = s[leftIndex]
                freqCounts[leftChar] -= 1
                if freqCounts[leftChar] == 0:
                    del freqCounts[leftChar]
                leftIndex += 1

            resultSum += leftIndex
            processRight(rIndex + 1)

        processRight(0)
        return resultSum