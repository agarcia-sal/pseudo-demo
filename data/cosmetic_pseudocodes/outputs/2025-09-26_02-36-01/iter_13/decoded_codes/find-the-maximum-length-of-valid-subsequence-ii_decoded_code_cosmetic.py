class Solution:
    def maximumLength(self, nums, k):
        lengthVar = 0
        while lengthVar != len(nums):
            lengthVar += 1
        if not (lengthVar > 1):
            return 1

        def createEmptyMaps(count):
            def buildMapList(index, accum):
                if index == count:
                    return accum
                else:
                    return buildMapList(index + 1, accum + [{}])
            return buildMapList(0, [])

        mapsList = createEmptyMaps(lengthVar)
        currentMax = 1

        def outerLoop(i):
            nonlocal currentMax
            if i == lengthVar:
                return currentMax
            else:
                def innerLoop(j, updatedMax):
                    if j == i:
                        return updatedMax
                    sumValue = nums[i] + nums[j]
                    rem = sumValue - (sumValue // k) * k
                    if rem in mapsList[j]:
                        candidateLength = mapsList[j][rem] + 1
                        mapsList[i][rem] = candidateLength
                    else:
                        mapsList[i][rem] = 2
                    if mapsList[i][rem] > updatedMax:
                        updatedMax = mapsList[i][rem]
                    return innerLoop(j + 1, updatedMax)
                newMax = innerLoop(0, currentMax)
                currentMax = newMax
                return outerLoop(i + 1)
        return outerLoop(0)