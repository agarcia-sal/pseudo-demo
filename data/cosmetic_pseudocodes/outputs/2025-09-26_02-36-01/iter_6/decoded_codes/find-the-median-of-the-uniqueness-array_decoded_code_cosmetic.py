class Solution:
    def medianOfUniquenessArray(self, nums):
        def tallyUpTo(bound):
            def incrementCount(dct, k):
                dct[k] = dct.get(k, 0) + 1

            def decrementCount(dct, k):
                dct[k] -= 1

            accumTotal = 0
            startIndex = 0
            frequencyMap = {}
            uniqueTotal = 0
            endIndex = 0

            def slideWindow():
                nonlocal accumTotal, startIndex, frequencyMap, uniqueTotal, endIndex
                if endIndex < len(nums):
                    if frequencyMap.get(nums[endIndex], 0) == 0:
                        uniqueTotal += 1
                    incrementCount(frequencyMap, nums[endIndex])
                    while uniqueTotal > bound:
                        decrementCount(frequencyMap, nums[startIndex])
                        if frequencyMap[nums[startIndex]] == 0:
                            uniqueTotal -= 1
                        startIndex += 1
                    accumTotal += (endIndex - startIndex + 1)
                    endIndex += 1
                    slideWindow()

            slideWindow()
            return accumTotal

        nSquared = len(nums) * (len(nums) + 1)
        totalSubs = nSquared // 2
        medianPos = (totalSubs + 1) // 2
        lowBound = 1
        highBound = len(nums)

        def binarySearch():
            nonlocal lowBound, highBound
            while lowBound < highBound:
                midVal = (lowBound + highBound) // 2
                if tallyUpTo(midVal) < medianPos:
                    lowBound = midVal + 1
                else:
                    highBound = midVal

        binarySearch()
        return lowBound