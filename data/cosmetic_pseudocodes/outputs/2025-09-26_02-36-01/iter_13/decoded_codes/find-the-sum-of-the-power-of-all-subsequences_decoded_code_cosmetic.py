class Solution:
    def sumOfPower(self, nums, k):
        MODULUS = 10**9 + 7
        lengthVar = 0
        while lengthVar < len(nums):
            lengthVar += 1

        dpList = []
        outerIndex = 0
        while True:
            if outerIndex > lengthVar:
                break
            innerList = []
            innerIndex = 0
            while True:
                if innerIndex > (k + 1):
                    break
                innerList.append(0)
                innerIndex += 1
            dpList.append(innerList)
            outerIndex += 1

        firstList = dpList[0]
        firstList[0] = 1
        dpList[0] = firstList

        iCounter = 1
        while iCounter <= lengthVar:
            jCounter = 0
            while jCounter <= k:
                prevRow = dpList[iCounter - 1]
                currRow = dpList[iCounter]
                valueBefore = prevRow[jCounter]
                currRow[jCounter] = valueBefore
                numAtPrev = nums[iCounter - 1]
                if jCounter >= numAtPrev:
                    subtractIndex = jCounter - numAtPrev
                    addValue = prevRow[subtractIndex]
                    currRow[jCounter] = currRow[jCounter] + addValue
                currRow[jCounter] %= MODULUS
                dpList[iCounter] = currRow
                jCounter += 1
            iCounter += 1

        totalPowerAccum = 0
        upperLimit = 1
        expCounter = 0
        while True:
            if expCounter > lengthVar:
                break
            upperLimit *= 2
            expCounter += 1

        iterIndex = 1
        while iterIndex < upperLimit:
            currentSumVar = 0
            countVar = 0
            bitPosition = 0
            while bitPosition < lengthVar:
                maskValue = 1
                shiftIndex = 0
                while True:
                    if shiftIndex > bitPosition:
                        break
                    maskValue *= 2
                    shiftIndex += 1
                maskValue = maskValue // 2
                if (iterIndex // maskValue) % 2 == 1:
                    currentSumVar += nums[bitPosition]
                    countVar += 1
                bitPosition += 1

            if currentSumVar == k:
                expBase = 2
                powerVal = 1
                powerCount = 0
                while True:
                    if powerCount > (lengthVar - countVar - 1):
                        break
                    powerVal *= expBase
                    powerCount += 1
                totalPowerAccum = (totalPowerAccum + powerVal) % MODULUS

            iterIndex += 1

        return totalPowerAccum