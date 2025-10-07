class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        freqMap = {}
        charIter = 0
        while charIter < len(s):
            currChar = s[charIter]
            if currChar in freqMap:
                freqMap[currChar] += 1
            else:
                freqMap[currChar] = 1
            charIter += 1

        maxObservedFreq = 0
        for freqVal in freqMap.values():
            if freqVal > maxObservedFreq:
                maxObservedFreq = freqVal

        candidateChars = set()
        for pairChar, pairFreq in freqMap.items():
            if pairFreq == maxObservedFreq:
                candidateChars.add(pairChar)

        collectedList = []

        def traverseReverse(position):
            if position < 0:
                return
            currSymbol = s[position]
            if currSymbol in candidateChars:
                collectedList.append(currSymbol)
                candidateChars.remove(currSymbol)
            traverseReverse(position - 1)

        traverseReverse(len(s) - 1)

        outputString = ""
        outputIndex = len(collectedList) - 1
        while outputIndex >= 0:
            outputString += collectedList[outputIndex]
            outputIndex -= 1

        return outputString