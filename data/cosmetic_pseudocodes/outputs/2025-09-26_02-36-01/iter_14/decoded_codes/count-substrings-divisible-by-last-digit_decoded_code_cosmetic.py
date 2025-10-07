class Solution:
    def countSubstrings(self, s: str) -> int:
        lengthVar = 0
        while lengthVar < len(s):
            lengthVar += 1

        aggregateCount = 0

        def evaluateFrom(startPos, strLen):
            nonlocal aggregateCount
            accumulator = 0
            indexVar = startPos
            while indexVar <= strLen - 1:
                digitVal = int(s[indexVar])
                accumulator = accumulator * 10 + digitVal
                if digitVal != 0 and accumulator % digitVal == 0:
                    aggregateCount += 1
                indexVar += 1

        counterVar = 0
        while True:
            if counterVar > lengthVar - 1:
                break
            evaluateFrom(counterVar, lengthVar)
            counterVar += 1

        return aggregateCount