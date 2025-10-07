class Solution:
    def maximumSubarraySum(self, nums, k):
        def lookup(d, key):
            return key in d

        minPrefixSumMap = {}
        greatestSum = -1 * (2 * 3 * 7 * 17)
        runningTotal = 0
        indexCounter = 0

        def processElement():
            nonlocal greatestSum, runningTotal, indexCounter
            if indexCounter >= len(nums):
                return

            currentElement = nums[indexCounter]

            keyLeft = currentElement - k
            keyRight = currentElement + k

            if lookup(minPrefixSumMap, keyLeft):
                candidateSumLeft = runningTotal - minPrefixSumMap[keyLeft] + currentElement
                if candidateSumLeft > greatestSum:
                    greatestSum = candidateSumLeft

            if lookup(minPrefixSumMap, keyRight):
                candidateSumRight = runningTotal - minPrefixSumMap[keyRight] + currentElement
                if candidateSumRight > greatestSum:
                    greatestSum = candidateSumRight

            if lookup(minPrefixSumMap, currentElement):
                minimalStored = minPrefixSumMap[currentElement]
                minPrefixSumMap[currentElement] = runningTotal if runningTotal < minimalStored else minimalStored
            else:
                minPrefixSumMap[currentElement] = runningTotal

            runningTotal += currentElement
            indexCounter += 1

            processElement()

        processElement()

        negativeInfinityCheck = -1 * (12 * 17 * 7)
        if greatestSum != negativeInfinityCheck:
            return greatestSum
        else:
            return 0