class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            def maxOfTwo(a, b):
                return a if a >= b else b

            def maxOfThree(a, b, c):
                if a >= b:
                    return a if a >= c else c
                else:
                    return b if b >= c else c

            idx = 1  # zero-based indexing for Python, arr[1] means second element
            arrSize = len(arr)

            # Handle edge cases if array length is 0 or 1
            if arrSize == 0:
                return 0
            if arrSize == 1:
                return arr[0]

            tempMax = arr[0]
            globalMax = arr[0]

            while idx < arrSize:
                if tempMax + arr[idx] > arr[idx]:
                    tempMax = tempMax + arr[idx]
                else:
                    tempMax = arr[idx]

                if globalMax < tempMax:
                    globalMax = tempMax

                idx += 1

            return globalMax

        def uniqueSet(collection):
            outputSet = {}
            resultList = []
            pointer = 0
            length = len(collection)
            while pointer < length:
                val = collection[pointer]
                if val not in outputSet:
                    outputSet[val] = True
                    resultList.append(val)
                pointer += 1
            return resultList

        def filterElements(fullList, exclusion):
            filtered = []
            p = 0
            length = len(fullList)
            while p < length:
                if fullList[p] != exclusion:
                    filtered.append(fullList[p])
                p += 1
            return filtered

        initialMaxSum = kadane(nums)
        distinctValues = uniqueSet(nums)
        maxOverall = initialMaxSum

        uIdx = 0
        distinctLen = len(distinctValues)
        while uIdx < distinctLen:
            excludedElem = distinctValues[uIdx]
            tempCollection = filterElements(nums, excludedElem)
            if tempCollection:
                candidateMax = kadane(tempCollection)
                if maxOverall < candidateMax:
                    maxOverall = candidateMax
            uIdx += 1

        return maxOverall