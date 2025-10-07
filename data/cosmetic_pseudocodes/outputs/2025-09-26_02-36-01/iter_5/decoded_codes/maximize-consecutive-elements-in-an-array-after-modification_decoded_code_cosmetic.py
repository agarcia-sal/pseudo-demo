class Solution:
    def maxSelectedElements(self, nums):
        maximumCount = 0
        storageMap = {}

        def processIndex(index, sortedList, currentResult):
            if index >= len(sortedList):
                return currentResult
            currentNumber = sortedList[index]

            valPlusOneKey = storageMap.get(currentNumber + 1, 0)
            storageMap[currentNumber + 1] = valPlusOneKey + 1

            valAtKeyMinusOne = storageMap.get(currentNumber - 1, 0)
            storageMap[currentNumber] = valAtKeyMinusOne + 1

            maxAmongValues = max(currentResult, storageMap[currentNumber], storageMap[currentNumber + 1])

            return processIndex(index + 1, sortedList, maxAmongValues)

        sortedNums = sorted(nums)
        maximumCount = processIndex(0, sortedNums, maximumCount)
        return maximumCount