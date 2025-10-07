class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        frequencyMap = {}
        resultValue = 0
        leftIndex = 0
        currentIndex = 0

        while currentIndex < len(s):
            currentChar = s[currentIndex]
            frequencyMap[currentChar] = frequencyMap.get(currentChar, 0) + 1

            shouldShrink = False
            for key in frequencyMap:
                if frequencyMap[key] >= k:
                    shouldShrink = True
                    break

            while shouldShrink:
                leftChar = s[leftIndex]
                frequencyMap[leftChar] -= 1
                if frequencyMap[leftChar] == 0:
                    del frequencyMap[leftChar]
                leftIndex += 1

                shouldShrink = False
                for key in frequencyMap:
                    if frequencyMap[key] >= k:
                        shouldShrink = True
                        break

            resultValue += leftIndex
            currentIndex += 1

        return resultValue