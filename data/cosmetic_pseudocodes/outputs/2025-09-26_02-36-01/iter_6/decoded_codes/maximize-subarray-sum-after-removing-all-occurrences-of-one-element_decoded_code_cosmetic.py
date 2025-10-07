class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            def maxOf(a, b):
                return a if a > b else b

            def sumOrSingle(a, b):
                return a if a >= a + b else a + b

            lengthArr = len(arr)

            def kadaneHelper(index, currentMax, globalMax):
                if index == lengthArr:
                    return globalMax
                currentElement = arr[index]
                candidateMax = sumOrSingle(currentMax, currentElement)
                nextCurrentMax = candidateMax
                nextGlobalMax = maxOf(globalMax, candidateMax)
                return kadaneHelper(index + 1, nextCurrentMax, nextGlobalMax)

            firstElement = arr[0]
            return kadaneHelper(1, firstElement, firstElement)

        def createSetFromList(lst):
            resultSet = {}
            index = 0
            length = len(lst)
            while index < length:
                elem = lst[index]
                if elem not in resultSet:
                    resultSet[elem] = True
                index += 1
            keyList = []
            for key in resultSet:
                keyList.append(key)
            return keyList

        maxSum = kadane(nums)
        uniques = createSetFromList(nums)

        def filterListExcluding(value, originalList, idx, accum):
            if idx >= len(originalList):
                return accum
            currentVal = originalList[idx]
            if currentVal != value:
                accum = accum + [currentVal]
            return filterListExcluding(value, originalList, idx + 1, accum)

        uniqueIndex = 0
        currentMaxSum = maxSum

        while uniqueIndex < len(uniques):
            suppressVal = uniques[uniqueIndex]
            filteredNums = filterListExcluding(suppressVal, nums, 0, [])

            filteredLen = len(filteredNums)

            if filteredLen != 0:
                candidateSum = kadane(filteredNums)
                if currentMaxSum < candidateSum:
                    currentMaxSum = candidateSum

            uniqueIndex += 1

        return currentMaxSum