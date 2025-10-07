class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(target):
            totalCount = 0
            startIdx = 0
            freqMap = {}
            uniqueCounter = 0

            for currentPos, currentVal in enumerate(nums):
                if freqMap.get(currentVal, 0) == 0:
                    uniqueCounter += 1
                freqMap[currentVal] = freqMap.get(currentVal, 0) + 1

                while uniqueCounter > target:
                    startVal = nums[startIdx]
                    freqMap[startVal] -= 1
                    if freqMap[startVal] == 0:
                        uniqueCounter -= 1
                    startIdx += 1

                totalCount += (currentPos - startIdx + 1)
            return totalCount

        n = len(nums)
        maxSubarrays = n * (n + 1) // 2
        medianPos = (maxSubarrays + 1) // 2
        lowBound, highBound = 1, n

        while lowBound < highBound:
            midVal = (lowBound + highBound) // 2
            cnt = countLessOrEqual(midVal)
            if cnt < medianPos:
                lowBound = midVal + 1
            else:
                highBound = midVal

        return lowBound