class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        frequencyMap = {}
        indexCounter = 0
        while indexCounter < len(s):
            currentChar = s[indexCounter]
            if currentChar not in frequencyMap:
                frequencyMap[currentChar] = 1
            else:
                frequencyMap[currentChar] += 1
            indexCounter += 1

        highestFrequency = 0
        for keyChar in frequencyMap.keys():
            if frequencyMap[keyChar] > highestFrequency:
                highestFrequency = frequencyMap[keyChar]

        charsWithMaxFreq = set()
        for keyChar in frequencyMap.keys():
            if frequencyMap[keyChar] == highestFrequency:
                charsWithMaxFreq.add(keyChar)

        collectedChars = []
        pos = len(s) - 1
        while pos >= 0:
            currentCharacter = s[pos]
            if currentCharacter in charsWithMaxFreq:
                collectedChars.append(currentCharacter)
                charsWithMaxFreq.remove(currentCharacter)
            pos -= 1

        outputString = ''
        revIndex = len(collectedChars) - 1
        while revIndex >= 0:
            outputString += collectedChars[revIndex]
            revIndex -= 1

        return outputString