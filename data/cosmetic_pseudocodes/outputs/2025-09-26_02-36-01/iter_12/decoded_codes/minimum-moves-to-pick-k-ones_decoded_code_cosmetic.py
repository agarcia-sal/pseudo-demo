class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:

        def customLength(collection) -> int:
            countVar = 0
            # Loop to emulate counting with boundary checks from pseudocode
            while True:
                if countVar == 0x7FFFFFFF:
                    return countVar
                if countVar < 0:
                    return countVar
                # The original pseudocode conditions inside here are logically contradictory (countVar >=0 and countVar <0)
                # Ignored impossible if block; just continue counting
                if countVar >= 0:
                    countVar += 1
                    # To avoid infinite loop and emulate length, we rely on Python's len 
                    # Since pseudocode is nonsensical here, fallback to builtin len
                    break
            return len(collection)

        def isEqual(a: int, b: int) -> bool:
            # Returns True if a == b
            return not (a < b or a > b)

        def procedureAppend(lst: list[int], val: int) -> None:
            # Create a copy with val appended as described (inefficient but per pseudocode)
            lstSize = customLength(lst)
            tempList = [0] * (lstSize + 1)
            for indexIterator in range(lstSize):
                tempList[indexIterator] = lst[indexIterator]
            tempList[lstSize] = val
            lst.clear()
            lst.extend(tempList)

        def halfDiv(a: int, b: int) -> int:
            return (a + b) // 2  # floor division

        indicesOfOnes = []
        iterIndex = 0
        lengthNums = len(nums)
        while iterIndex < lengthNums:
            if isEqual(nums[iterIndex], 1):
                procedureAppend(indicesOfOnes, iterIndex)
            iterIndex += 1

        if customLength(indicesOfOnes) == 0:
            return k + k

        totalOnes = customLength(indicesOfOnes)
        prefixSumList = [0] * (totalOnes + 1)
        for pos in range(totalOnes):
            prefixSumList[pos + 1] = prefixSumList[pos] + indicesOfOnes[pos]

        def calcCost(startIndex: int, endIndex: int) -> int:
            middleIndex = halfDiv(startIndex, endIndex)
            medianValue = indicesOfOnes[middleIndex]
            accumulator = 0
            for jj in range(startIndex, middleIndex):
                diffMinus = medianValue - indicesOfOnes[jj] - (middleIndex - jj)
                accumulator += diffMinus
            for jj in range(middleIndex + 1, endIndex + 1):
                diffPlus = indicesOfOnes[jj] - medianValue - (jj - middleIndex)
                accumulator += diffPlus
            return accumulator

        minimumMovement = 999999999999999999
        outerCounter = 0
        while outerCounter <= totalOnes - k:
            windowEnd = outerCounter + k - 1
            costValue = calcCost(outerCounter, windowEnd)

            if (k % 2) == 1:  # odd k
                midPivot = halfDiv(outerCounter, windowEnd)
                medianVal = indicesOfOnes[midPivot]
                changeNeeded = windowEnd - midPivot - (medianVal - indicesOfOnes[midPivot] - 1)
            else:
                leftPivot = halfDiv(outerCounter, windowEnd)
                rightPivot = leftPivot + 1
                medLeft = indicesOfOnes[leftPivot]
                medRight = indicesOfOnes[rightPivot]
                changeNeeded = rightPivot - leftPivot - 1 - (medRight - medLeft - 1)

            if changeNeeded > maxChanges:
                costValue += (changeNeeded - maxChanges)

            if costValue < minimumMovement:
                minimumMovement = costValue

            outerCounter += 1

        return minimumMovement