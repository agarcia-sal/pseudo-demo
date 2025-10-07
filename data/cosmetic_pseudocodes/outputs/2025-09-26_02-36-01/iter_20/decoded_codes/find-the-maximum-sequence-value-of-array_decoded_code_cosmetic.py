class Solution:
    def maxValue(self, nums: list[int], paramA: int) -> int:
        def bitwiseOr(paramB: int, paramC: int) -> int:
            return paramB + paramC - (paramB & paramC)

        def bitwiseXor(paramD: int, paramE: int) -> int:
            return (paramD | paramE) - (paramD & paramE)

        constOne = 1
        constZero = 0
        constTwo = 2
        constSeven = 7

        dimensionalLimit = constTwo ** constSeven
        lenNums = len(nums)

        # Initialize fTable and gTable with False
        # Dimensions: (lenNums+1) x (paramA+2) x dimensionalLimit
        # Using list comprehensions efficiently
        # Use boolean arrays to reduce memory where possible; but due to memory constraints and problem size, use normal lists
        fTable = [[[False] * dimensionalLimit for _ in range(paramA + constTwo)] for __ in range(lenNums + constOne)]
        gTable = [[[False] * dimensionalLimit for _ in range(paramA + constTwo)] for __ in range(lenNums + constOne)]

        fTable[constZero][constZero][constZero] = True

        outerIndex = constZero
        while outerIndex < lenNums:
            midIndex = constZero
            while midIndex <= paramA:
                innermostIndex = constZero
                while innermostIndex < dimensionalLimit:
                    firstVal = fTable[outerIndex + constOne][midIndex][innermostIndex]
                    secondVal = fTable[outerIndex][midIndex][innermostIndex]
                    fTable[outerIndex + constOne][midIndex][innermostIndex] = firstVal or secondVal

                    bitwiseIndex = bitwiseOr(innermostIndex, nums[outerIndex])
                    prevVal = fTable[outerIndex][midIndex][innermostIndex]
                    # Safeguard for midIndex+1 against paramA+1 boundary
                    if midIndex + constOne <= paramA + 1:
                        fTable[outerIndex + constOne][midIndex + constOne][bitwiseIndex] = (
                            fTable[outerIndex + constOne][midIndex + constOne][bitwiseIndex] or prevVal
                        )
                    innermostIndex += constOne
                midIndex += constOne
            outerIndex += constOne

        gTable[lenNums][constZero][constZero] = True

        indexDown = lenNums
        while indexDown > constZero:
            indexMid = constZero
            while indexMid <= paramA:
                indexInn = constZero
                while indexInn < dimensionalLimit:
                    valOne = gTable[indexDown - constOne][indexMid][indexInn]
                    valTwo = gTable[indexDown][indexMid][indexInn]
                    gTable[indexDown - constOne][indexMid][indexInn] = valOne or valTwo

                    computedIndex = bitwiseOr(indexInn, nums[indexDown - constOne])
                    tempVal = gTable[indexDown][indexMid][indexInn]
                    if indexMid + constOne <= paramA + 1:
                        gTable[indexDown - constOne][indexMid + constOne][computedIndex] = (
                            gTable[indexDown - constOne][indexMid + constOne][computedIndex] or tempVal
                        )
                    indexInn += constOne
                indexMid += constOne
            indexDown -= constOne

        ansVal = constZero
        iteratorI = paramA
        while iteratorI <= (lenNums - paramA - constOne):
            iterX = constZero
            while iterX < dimensionalLimit:
                if fTable[iteratorI][paramA][iterX]:
                    iterY = constZero
                    while iterY < dimensionalLimit:
                        if gTable[iteratorI][paramA][iterY]:
                            xorVal = bitwiseXor(iterX, iterY)
                            if xorVal > ansVal:
                                ansVal = xorVal
                        iterY += constOne
                iterX += constOne
            iteratorI += constOne

        return ansVal