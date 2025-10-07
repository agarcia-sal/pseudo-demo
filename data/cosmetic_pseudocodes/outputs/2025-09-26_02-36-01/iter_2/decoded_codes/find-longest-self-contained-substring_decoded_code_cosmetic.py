class Solution:
    def maxSubstringLength(self, s: str) -> int:
        totalFrequencies = {}
        for ch in s:
            totalFrequencies[ch] = totalFrequencies.get(ch, 0) + 1

        resultMax = -1
        n = len(s)
        for startIdx in range(n):
            partialFrequencies = {}
            for endIdx in range(startIdx, n):
                currentChar = s[endIdx]
                partialFrequencies[currentChar] = partialFrequencies.get(currentChar, 0) + 1

                # Check if for all chars in partialFrequencies,
                # their count >= corresponding count in totalFrequencies
                allKeysMeetCondition = True
                for keyChar in partialFrequencies:
                    if partialFrequencies[keyChar] < totalFrequencies[keyChar]:
                        allKeysMeetCondition = False
                        break

                if allKeysMeetCondition and len(partialFrequencies) < len(totalFrequencies):
                    substringLength = (endIdx - startIdx) + 1
                    if substringLength > resultMax:
                        resultMax = substringLength

        return resultMax