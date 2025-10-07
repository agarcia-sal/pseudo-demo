class Solution:
    def minValidStrings(self, words, target):
        def isInSet(strVal, setVal):
            return strVal in setVal

        alphaSet = set()
        idxA = 0
        lengthTarget = len(target)

        while idxA < len(words):
            currentWord = words[idxA]
            lengthWord = len(currentWord)

            positionB = 1
            while positionB <= lengthWord:
                tempStr = ""
                positionC = 0
                while positionC < positionB:
                    tempStr += currentWord[positionC]
                    positionC += 1
                alphaSet.add(tempStr)
                positionB += 1

            idxA += 1

        dpArray = [float('inf')] * (lengthTarget + 1)
        dpArray[0] = 0

        idxA = 1
        while idxA <= lengthTarget:
            idxB = 1
            while idxB <= idxA:
                subStr = ""
                positionC = idxB - 1
                while positionC < idxA:
                    subStr += target[positionC]
                    positionC += 1

                if isInSet(subStr, alphaSet):
                    candidateVal = dpArray[idxB - 1] + 1
                    if candidateVal < dpArray[idxA]:
                        dpArray[idxA] = candidateVal
                idxB += 1
            idxA += 1

        return dpArray[lengthTarget] if dpArray[lengthTarget] < float('inf') else -1