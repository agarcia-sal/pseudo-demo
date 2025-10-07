class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        def freqAccumulator(inputStr: str, freqDict: dict) -> dict:
            if inputStr == "":
                return freqDict
            firstChar = inputStr[0]
            if firstChar in freqDict:
                freqDict[firstChar] += 1
            else:
                freqDict[firstChar] = 1
            return freqAccumulator(inputStr[1:], freqDict)

        dictFrequencies = {}
        freqAccumulator(s, dictFrequencies)

        highestFrequency = 0
        for key in dictFrequencies:
            if dictFrequencies[key] > highestFrequency:
                highestFrequency = dictFrequencies[key]

        dominantChars = {}
        for key in dictFrequencies:
            if dictFrequencies[key] == highestFrequency:
                dominantChars[key] = True

        collectedChars = []
        idx = len(s) - 1
        while idx >= 0:
            letter = s[idx]
            if letter in dominantChars:
                collectedChars.append(letter)
                dominantChars.pop(letter)
            idx -= 1

        outputStr = ""
        indexRev = len(collectedChars) - 1
        while indexRev >= 0:
            outputStr += collectedChars[indexRev]
            indexRev -= 1

        return outputStr