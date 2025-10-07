from collections import Counter as CountElements

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        tempMap = CountElements(s)
        tempMap.pop("?", None)

        idxCollection = []
        posCounter = 0
        while posCounter < len(s):
            currentCh = s[posCounter]
            if currentCh == "?":
                idxCollection.append(posCounter)
            posCounter += 1

        assignedChars = []
        loopPos = 0
        while loopPos < len(idxCollection):
            minimalCount = float('inf')
            chosenChar = None

            letterIdx = 0
            while letterIdx <= 25:
                candidateChar = chr(ord("a") + letterIdx)

                currentCount = tempMap[candidateChar] if candidateChar in tempMap else 0

                if currentCount < minimalCount:
                    minimalCount = currentCount
                    chosenChar = candidateChar

                letterIdx += 1

            assignedChars.append(chosenChar)
            if chosenChar in tempMap:
                tempMap[chosenChar] += 1
            else:
                tempMap[chosenChar] = 1

            loopPos += 1

        sortedAssignedChars = assignedChars[:]
        changed = True
        while changed:
            changed = False
            i = 1
            while i < len(sortedAssignedChars):
                if sortedAssignedChars[i - 1] > sortedAssignedChars[i]:
                    tempChar = sortedAssignedChars[i - 1]
                    sortedAssignedChars[i - 1] = sortedAssignedChars[i]
                    sortedAssignedChars[i] = tempChar
                    changed = True
                i += 1

        charArray = []
        j = 0
        while j < len(s):
            charArray.append(s[j])
            j += 1

        k = 0
        while k < len(idxCollection):
            position = idxCollection[k]
            charArray[position] = sortedAssignedChars[k]
            k += 1

        resultString = ""
        l = 0
        while l < len(charArray):
            resultString += charArray[l]
            l += 1

        return resultString