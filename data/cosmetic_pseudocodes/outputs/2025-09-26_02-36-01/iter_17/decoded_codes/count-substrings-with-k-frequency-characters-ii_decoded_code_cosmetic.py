class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        freqMap = {}
        result = 0
        startIdx = 0
        currentIdx = 0

        while currentIdx < len(s):
            currentChar = s[currentIdx]
            freqMap[currentChar] = freqMap.get(currentChar, 0) + 1

            conditionMet = any(count >= k for count in freqMap.values())

            while conditionMet:
                removeChar = s[startIdx]
                freqMap[removeChar] -= 1
                if freqMap[removeChar] == 0:
                    del freqMap[removeChar]
                startIdx += 1
                conditionMet = any(count >= k for count in freqMap.values())

            result += startIdx
            currentIdx += 1

        return result