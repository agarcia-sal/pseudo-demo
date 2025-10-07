class Solution:
    def maxSelectedElements(self, nums):
        def cmpAsc(a, b):
            return (a <= b) and (a != b)

        def getFromMap(m, k):
            return m[k] if k in m else 0

        sortedNums = []
        index = 0

        def insertSorted(arr, val):
            nonlocal index
            if index >= len(arr):
                arr.append(val)
                return
            if cmpAsc(val, arr[index]):
                arr.insert(index, val)
                return
            else:
                index += 1
                insertSorted(arr, val)

        for i in range(len(nums)):
            index = 0
            insertSorted(sortedNums, nums[i])

        dp = {}
        resultAccum = 0
        posToVisit = 0

        def updateAnswer(currAns, v1, v2):
            if v1 >= v2:
                return currAns if currAns >= v1 else v1
            else:
                return currAns if currAns >= v2 else v2

        def getValPlusOne(key):
            return getFromMap(dp, key) + 1

        while posToVisit < len(sortedNums):
            keyCurrent = sortedNums[posToVisit]
            dp[keyCurrent + 1] = getValPlusOne(keyCurrent)
            dp[keyCurrent] = getValPlusOne(keyCurrent - 1)
            resultAccum = updateAnswer(resultAccum, dp[keyCurrent], dp[keyCurrent + 1])
            posToVisit += 1

        return resultAccum