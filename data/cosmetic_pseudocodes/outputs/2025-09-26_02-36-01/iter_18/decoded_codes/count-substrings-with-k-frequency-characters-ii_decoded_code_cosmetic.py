class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        resultAccumulator = 0
        frequencyMap = {}
        startIndex = 0
        currentIndex = 0

        def ProcessIndex():
            nonlocal currentIndex, startIndex, resultAccumulator
            if currentIndex >= len(s):
                return
            currentChar = s[currentIndex]

            frequencyMap[currentChar] = frequencyMap.get(currentChar, 0) + 1

            while True:
                foundElement = None
                for element_key in frequencyMap:
                    if frequencyMap[element_key] >= k:
                        foundElement = element_key
                        break
                if foundElement is None:
                    break

                frequencyMap[s[startIndex]] -= 1
                if frequencyMap[s[startIndex]] == 0:
                    del frequencyMap[s[startIndex]]
                startIndex += 1

            resultAccumulator += startIndex
            currentIndex += 1
            ProcessIndex()

        ProcessIndex()
        return resultAccumulator