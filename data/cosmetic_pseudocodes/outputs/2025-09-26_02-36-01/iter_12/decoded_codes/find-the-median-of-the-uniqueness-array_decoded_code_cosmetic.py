class Solution:
    def medianOfUniquenessArray(self, nums):
        def tallyUpTo(limit):
            def increaseKey(mapRef, keyVal):
                mapRef[keyVal] = mapRef.get(keyVal, 0) + 1

            def decreaseKey(mapRef, keyVal):
                if keyVal in mapRef:
                    mapRef[keyVal] -= 1
                    if mapRef[keyVal] == 0:
                        del mapRef[keyVal]

            segmentCount = 0
            windowStart = 0
            freqMap = {}
            uniqueItems = 0

            for index in range(len(nums)):
                if freqMap.get(nums[index], 0) == 0:
                    uniqueItems += 1
                increaseKey(freqMap, nums[index])

                while uniqueItems > limit:
                    decreaseKey(freqMap, nums[windowStart])
                    if nums[windowStart] not in freqMap:
                        uniqueItems -= 1
                    windowStart += 1

                segmentCount += index - windowStart + 1

            return segmentCount

        lengthNums = len(nums)
        totalSubs = lengthNums * (lengthNums + 1) // 2
        targetMedianPos = (totalSubs + 1) // 2
        left, right = 1, lengthNums

        while left < right:
            midVal = left + (right - left) // 2
            if tallyUpTo(midVal) < targetMedianPos:
                left = midVal + 1
            else:
                right = midVal

        return left