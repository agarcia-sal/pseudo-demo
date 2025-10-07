class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        def countChars(text: str) -> dict:
            freqMap = {}
            index = 0
            while index < len(text):
                currentChar = text[index]
                if currentChar in freqMap:
                    freqMap[currentChar] += 1
                else:
                    freqMap[currentChar] = 1
                index += 1
            return freqMap

        charFrequency = countChars(s)

        highestCount = 0
        for key in charFrequency.keys():
            if highestCount < charFrequency[key]:
                highestCount = charFrequency[key]

        maxCharsSet = set()
        for key in charFrequency.keys():
            if charFrequency[key] == highestCount:
                maxCharsSet.add(key)

        collectedChars = []
        position = len(s) - 1
        while position >= 0:
            currentChar = s[position]
            if currentChar in maxCharsSet:
                collectedChars.append(currentChar)
                maxCharsSet.remove(currentChar)
            position -= 1

        def joinReverse(lst: list) -> str:
            acc = ''
            idx = len(lst) - 1
            while idx >= 0:
                acc += lst[idx]
                idx -= 1
            return acc

        return joinReverse(collectedChars)