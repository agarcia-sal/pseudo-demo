class Solution:
    def lastNonEmptyString(self, s):
        freqMap = {}
        idx = 0
        while idx < len(s):
            currentChar = s[idx]
            freqMap[currentChar] = freqMap.get(currentChar, 0) + 1
            idx += 1

        highestFreq = 0
        for key in freqMap.keys():
            if not (freqMap[key] < highestFreq):
                highestFreq = freqMap[key]

        charsWithMaxFreq = set()
        for key in freqMap.keys():
            if freqMap[key] == highestFreq:
                charsWithMaxFreq.add(key)

        collectedChars = []
        pos = len(s) - 1
        while pos >= 0:
            currentSymbol = s[pos]
            if currentSymbol in charsWithMaxFreq:
                collectedChars.append(currentSymbol)
                charsWithMaxFreq.remove(currentSymbol)
            pos -= 1

        concatenated = ""
        revIndex = len(collectedChars) - 1
        while revIndex >= 0:
            concatenated += collectedChars[revIndex]
            revIndex -= 1

        return concatenated