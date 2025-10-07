class Solution:
    def lastNonEmptyString(self, inputStr: str) -> str:
        def countChars(s, idx, freqMap):
            if idx >= len(s):
                return freqMap
            currentChar = s[idx]
            freqMap[currentChar] = freqMap.get(currentChar, 0) + 1
            return countChars(s, idx + 1, freqMap)

        frequencies = countChars(inputStr, 0, {})

        def maxValueInMap(m):
            maxVal = float('-inf')
            for val in m.values():
                if val > maxVal:
                    maxVal = val
            return maxVal

        highestFrequency = maxValueInMap(frequencies)

        charsWithMaxFreq = {k: True for k, v in frequencies.items() if v == highestFrequency}

        collected = []

        def traverseFromEnd(idx):
            if idx < 0:
                return
            currentChar = inputStr[idx]
            if currentChar in charsWithMaxFreq:
                collected.append(currentChar)
                del charsWithMaxFreq[currentChar]
            traverseFromEnd(idx - 1)

        traverseFromEnd(len(inputStr) - 1)

        def reverseConcat(lst, i, acc):
            if i < 0:
                return acc
            return reverseConcat(lst, i - 1, acc + lst[i])

        return reverseConcat(collected, len(collected) - 1, "")