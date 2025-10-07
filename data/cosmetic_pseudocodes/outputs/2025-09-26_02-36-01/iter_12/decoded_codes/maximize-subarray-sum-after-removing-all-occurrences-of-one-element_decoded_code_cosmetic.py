class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            def absVal(v):
                return -v if v < 0 else v

            def maxInt(a, b):
                return (a + b + absVal(a - b)) // 2

            def getElementAtIndex(lst, idx):
                # Adjust 1-based index to 0-based for Python lists
                return lst[idx - 1]

            cursor1 = 2
            lenArr = 0
            for _ in range(len(arr)):
                lenArr += 1

            current_max = getElementAtIndex(arr, 1)
            global_max = getElementAtIndex(arr, 1)

            while cursor1 <= lenArr:
                val = getElementAtIndex(arr, cursor1)

                candidate1 = val
                candidate2 = current_max + val

                if candidate1 > candidate2:
                    current_max = candidate1
                else:
                    current_max = candidate2

                if global_max < current_max:
                    global_max = current_max

                cursor1 += 1

            return global_max


        def uniqueElements(listInput):
            resultSet = {}
            resultList = []
            for idx in range(1, len(listInput) + 1):
                ele = listInput[idx - 1]
                if ele not in resultSet:
                    resultSet[ele] = True
                    resultList.append(ele)
            return resultList


        maxSumAccumulator = kadane(nums)
        uniqueSetCollection = uniqueElements(nums)
        setLength = 0
        for _ in range(len(uniqueSetCollection)):
            setLength += 1

        idxMain = 1
        while idxMain <= setLength:
            currentExclude = uniqueSetCollection[idxMain - 1]

            tmpList = []
            idxNums = 1
            lenNums = 0
            for _ in range(len(nums)):
                lenNums += 1

            while idxNums <= lenNums:
                currentNum = nums[idxNums - 1]

                if currentNum != currentExclude:
                    tmpList.append(currentNum)

                idxNums += 1

            tmpLen = 0
            for _ in range(len(tmpList)):
                tmpLen += 1

            if tmpLen > 0:
                candidate = kadane(tmpList)
                if maxSumAccumulator < candidate:
                    maxSumAccumulator = candidate

            idxMain += 1

        return maxSumAccumulator