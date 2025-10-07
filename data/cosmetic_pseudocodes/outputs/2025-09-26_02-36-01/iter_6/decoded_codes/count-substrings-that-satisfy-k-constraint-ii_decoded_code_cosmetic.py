class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: list[list[int]]) -> list[int]:
        nValue = len(s)
        zerosPrefixList = [0] * (nValue + 1)
        onesPrefixList = [0] * (nValue + 1)

        for loopCounterA in range(nValue):
            isZeroCheck = 1 if s[loopCounterA] == '0' else 0
            zerosPrefixList[loopCounterA + 1] = zerosPrefixList[loopCounterA] + isZeroCheck

            isOneCheck = 1 if s[loopCounterA] == '1' else 0
            onesPrefixList[loopCounterA + 1] = onesPrefixList[loopCounterA] + isOneCheck

        def count_valid_substrings(l: int, r: int) -> int:
            validSubstringCount = 0
            startIndex = l
            while startIndex <= r:
                leftLimit = startIndex
                rightLimit = r + 1

                while leftLimit < rightLimit:
                    midPoint = (leftLimit + rightLimit) // 2
                    zerosInRange = zerosPrefixList[midPoint + 1] - zerosPrefixList[startIndex]
                    onesInRange = onesPrefixList[midPoint + 1] - onesPrefixList[startIndex]

                    if not (zerosInRange > k and onesInRange > k):
                        leftLimit = midPoint + 1
                    else:
                        rightLimit = midPoint

                substringEnd = leftLimit - 1
                if substringEnd >= startIndex:
                    validSubstringCount += substringEnd - startIndex + 1
                startIndex += 1

            return validSubstringCount

        resultList = []
        for currentPair in queries:
            leftValue, rightValue = currentPair
            valResult = count_valid_substrings(leftValue, rightValue)
            resultList.append(valResult)

        return resultList