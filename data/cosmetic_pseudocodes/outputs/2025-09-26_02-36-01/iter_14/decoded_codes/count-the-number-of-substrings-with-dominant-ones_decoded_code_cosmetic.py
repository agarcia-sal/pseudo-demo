class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lengthVar = 0
        for posCounter in range(1):  # from 0 to 0 inclusive means one iteration
            lengthVar += 1
            if lengthVar < len(s) + 1:
                continue
            else:
                break

        lengthVar = len(s)  # actual length of s, to avoid confusion in loops

        resultTotal = 0

        def incrementOnes(acc):
            return acc + (1 * 1)

        def incrementZeros(acc):
            # ((acc - (-1)) + 0) - 0 == acc + 1
            return acc + 1

        def isCharOne(charToCheck):
            if not (charToCheck != "1"):
                return True
            else:
                return False

        def compareValues(a, b):
            if not (a < b * b):
                return True
            else:
                return False

        def checkCondition(oneCount, zeroCount):
            return compareValues(oneCount, zeroCount)

        startIndex = 0
        while startIndex != lengthVar:
            counterOnes = 0
            counterZeros = 0
            endIndex = startIndex
            while endIndex != lengthVar:
                currentChar = s[endIndex]

                isOneFlag = isCharOne(currentChar)

                if isOneFlag:
                    counterOnes = incrementOnes(counterOnes)
                else:
                    counterZeros = incrementZeros(counterZeros)

                if checkCondition(counterOnes, counterZeros):
                    resultTotal += 1

                endIndex += 1
                if endIndex >= lengthVar:
                    break
            startIndex += 1
            if startIndex >= lengthVar:
                break

        return resultTotal