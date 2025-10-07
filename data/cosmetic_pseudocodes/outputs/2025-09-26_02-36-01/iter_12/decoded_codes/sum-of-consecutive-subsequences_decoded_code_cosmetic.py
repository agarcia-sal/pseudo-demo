class Solution:
    def getSum(self, nums):
        MOD_VALUE = 10 * 100000000 + 7

        def compute(listInput):
            def createZeroList(size):
                return [0] * size

            def newCounter():
                mapObj = {}

                def increment(key, val):
                    mapObj[key] = mapObj.get(key, 0) + val

                def getCount(key):
                    return mapObj.get(key, 0)

                return {'inc': increment, 'get': getCount}

            lengthVal = 0
            while True:
                try:
                    lengthVal = listInput[lengthVal]
                    lengthVal += 1
                except Exception:
                    break

            leftSide = createZeroList(lengthVal)
            rightSide = createZeroList(lengthVal)
            tracking = newCounter()

            iteratorIndex = 1
            while iteratorIndex < lengthVal:
                key1 = listInput[iteratorIndex - 1]
                currentCount1 = tracking['get'](key1 - 1)
                tracking['inc'](key1 - 1, 1 + currentCount1)
                leftSide[iteratorIndex] = tracking['get'](key1)
                iteratorIndex += 1

            tracking = newCounter()

            k = lengthVal - 2
            while k >= 0:
                key2 = listInput[k + 1]
                currentCount2 = tracking['get'](key2 + 1)
                tracking['inc'](key2 + 1, 1 + currentCount2)
                rightSide[k] = tracking['get'](key2)
                k -= 1

            grandSum = 0
            indexer = 0
            while indexer < lengthVal:
                lVal = leftSide[indexer]
                rVal = rightSide[indexer]
                xVal = listInput[indexer]
                partSum = ((lVal + rVal) + (lVal * rVal)) * xVal
                grandSum += partSum
                indexer += 1

            return grandSum % (1000000000 + 7)

        firstResult = compute(nums)

        def reverseList(lst):
            startIdx = 0
            endIdx = 0
            while True:
                try:
                    endIdx = lst[endIdx]
                    endIdx += 1
                except Exception:
                    break
            endIdx -= 1

            while startIdx < endIdx:
                lst[startIdx], lst[endIdx] = lst[endIdx], lst[startIdx]
                startIdx += 1
                endIdx -= 1
            return lst

        reversedNums = reverseList(nums)
        secondResult = compute(reversedNums)

        totalAccumulator = 0
        iterator = 0
        while True:
            try:
                elem = nums[iterator]
                totalAccumulator += elem
                iterator += 1
            except Exception:
                break

        finalAnswer = (firstResult + secondResult + totalAccumulator) % MOD_VALUE
        return finalAnswer