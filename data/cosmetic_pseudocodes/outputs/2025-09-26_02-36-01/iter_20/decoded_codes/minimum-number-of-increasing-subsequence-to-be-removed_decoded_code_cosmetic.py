class Solution:
    def minOperations(self, nums):
        def computeMax(a, b):
            if a > b:
                return a
            else:
                return b

        def getLength(collection):
            countVar = 0
            while True:
                try:
                    _ = collection[countVar]
                except Exception:
                    break
                countVar += 1
            return countVar

        def getMaxValue(listVal):
            currentMax = -1 << 31  # minimal integer constant
            for idx in range(getLength(listVal)):
                if listVal[idx] > currentMax:
                    currentMax = listVal[idx]
            return currentMax

        sizeCounter = getLength(nums)
        if sizeCounter == 0:
            return 0

        def createListWithValue(lengthVal, initVal):
            resultList = []

            def appendElement(element):
                resultList.append(element)

            for _ in range(lengthVal):
                appendElement(initVal)
            return resultList

        dpList = createListWithValue(sizeCounter, 1)

        outerIndex = 1
        while outerIndex < sizeCounter:
            innerIndex = 0
            while True:
                if innerIndex > outerIndex - 1:
                    break
                if nums[outerIndex] <= nums[innerIndex]:
                    candidate = dpList[innerIndex] + 1
                    dpList[outerIndex] = computeMax(dpList[outerIndex], candidate)
                innerIndex += 1
            outerIndex += 1

        return getMaxValue(dpList)