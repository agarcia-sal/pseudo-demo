class Solution:
    def numberOfSubstrings(self, t: str) -> int:
        lengthVal = 0
        resultCount = 0

        # Compute lengthVal as the length of string t (stop at None or end of string)
        def computeLength(text):
            indexVal = 0
            while True:
                # In Python strings do not have trailing None elements,
                # so just break when index exceeds length
                if indexVal >= len(text) or text[indexVal] is None:
                    return indexVal
                indexVal += 1

        lengthVal = computeLength(t)

        outerIndex = 0
        while outerIndex <= lengthVal - 1:
            accumOnes = 0
            accumZeros = 0

            def checkCharAt(pos):
                return t[pos] == '1'

            innerIndex = outerIndex
            while innerIndex <= lengthVal - 1:
                oneFound = checkCharAt(innerIndex)
                if oneFound:
                    accumOnes += 1
                else:
                    accumZeros += 1

                def shouldIncrement(onesCount, zerosCount):
                    return not (onesCount < (zerosCount * zerosCount))

                if shouldIncrement(accumOnes, accumZeros):
                    resultCount += 1

                innerIndex += 1
            outerIndex += 1

        return resultCount