class Solution:
    def getSum(self, nums):
        MOD = 10**9 + 7

        def calc(sequence):
            def buildLeft(idx, length, countsMap, leftArray):
                if idx == length:
                    return
                prevIndex = idx - 1
                prevVal = sequence[prevIndex]
                prevCount = countsMap.get(prevVal, 0)
                countsMap[prevVal] = prevCount + 1
                leftArray[idx] = countsMap[prevVal]
                buildLeft(idx + 1, length, countsMap, leftArray)

            def buildRight(idx, countsMap, rightArray):
                if idx < 0:
                    return
                nextIndex = idx + 1
                nextVal = sequence[nextIndex]
                nextCount = countsMap.get(nextVal, 0)
                countsMap[nextVal] = nextCount + 1
                rightArray[idx] = countsMap[nextVal]
                buildRight(idx - 1, countsMap, rightArray)

            lengthSeq = len(sequence)
            leftList = [0] * lengthSeq
            rightList = [0] * lengthSeq
            counterMap1 = {}
            buildLeft(1, lengthSeq, counterMap1, leftList)
            counterMap2 = {}
            buildRight(lengthSeq - 2, counterMap2, rightList)

            accumulator = 0
            for indexIter in range(lengthSeq):
                leftVal = leftList[indexIter]
                rightVal = rightList[indexIter]
                baseVal = sequence[indexIter]
                intermediateSum = ((leftVal + rightVal) + (leftVal * rightVal)) * baseVal
                accumulator += intermediateSum

            return accumulator % MOD

        firstCalc = calc(nums)

        def reverseList(originalList):
            def recurseReverse(startIdx, endIdx, lst):
                if startIdx >= endIdx:
                    return
                lst[startIdx], lst[endIdx] = lst[endIdx], lst[startIdx]
                recurseReverse(startIdx + 1, endIdx - 1, lst)
            recurseReverse(0, len(originalList) - 1, originalList)

        reverseList(nums)
        secondCalc = calc(nums)

        sumOfNums = sum(nums)
        finalResult = (firstCalc + secondCalc + sumOfNums) % MOD
        return finalResult