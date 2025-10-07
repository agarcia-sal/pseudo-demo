from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        frequencyMap = defaultdict(int)
        resultAccumulator = 0
        leftIndex = 0
        currentIndex = 0
        n = len(s)

        while currentIndex < n:
            currentChar = s[currentIndex]
            frequencyMap[currentChar] += 1

            # While there exists a key whose count is NOT less than k (i.e., >= k),
            # shrink the window from the left
            while any(count >= k for count in frequencyMap.values()):
                leftChar = s[leftIndex]
                frequencyMap[leftChar] -= 1
                if frequencyMap[leftChar] == 0:
                    del frequencyMap[leftChar]
                leftIndex += 1

            resultAccumulator += leftIndex
            currentIndex += 1

        return resultAccumulator