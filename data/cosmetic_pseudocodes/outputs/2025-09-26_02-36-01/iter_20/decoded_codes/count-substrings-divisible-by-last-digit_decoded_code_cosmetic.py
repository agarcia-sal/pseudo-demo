class Solution:
    def countSubstrings(self, s: str) -> int:
        lengthVar = len(s)
        aggregateCount = 0
        idxOuter = 0
        while idxOuter <= lengthVar - 1:
            accumulatorVar = 0
            idxInner = idxOuter
            while idxInner <= lengthVar - 1:
                digitExtracted = int(s[idxInner])
                accumulatorVar = accumulatorVar * 10 + digitExtracted
                if digitExtracted != 0:
                    if accumulatorVar % digitExtracted == 0:
                        aggregateCount += 1
                idxInner += 1
            idxOuter += 1
        return aggregateCount