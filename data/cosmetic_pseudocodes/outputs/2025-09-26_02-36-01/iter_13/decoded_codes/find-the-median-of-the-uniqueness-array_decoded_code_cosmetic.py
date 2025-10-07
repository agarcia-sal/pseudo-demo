class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(target):
            tally = {}
            leftIdx = 0
            uniqueCount = 0
            accCount = 0

            for i, numVal in enumerate(nums):
                # Increment count for numVal
                if numVal not in tally:
                    tally[numVal] = 0
                if tally[numVal] == 0:
                    uniqueCount += 1
                tally[numVal] += 1

                # Shrink window from left while uniqueCount > target
                while uniqueCount > target:
                    leftVal = nums[leftIdx]
                    tally[leftVal] -= 1
                    if tally[leftVal] == 0:
                        uniqueCount -= 1
                    leftIdx += 1

                accCount += (i - leftIdx + 1)

            return accCount

        n = len(nums)
        totalSubs = n * (n + 1) // 2
        medianPos = (totalSubs + 1) // 2
        lowBound = 1
        highBound = n

        while lowBound < highBound:
            midVal = (lowBound + highBound) // 2
            cmpVal = countLessOrEqual(midVal)
            if cmpVal < medianPos:
                lowBound = midVal + 1
            else:
                highBound = midVal

        return lowBound