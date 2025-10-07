from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(target):
            totalCount = 0
            startIdx = 0
            freqMap = defaultdict(int)
            uniqElems = 0
            for endIdx, currentNum in enumerate(nums):
                if freqMap[currentNum] == 0:
                    uniqElems += 1
                freqMap[currentNum] += 1
                while uniqElems > target:
                    leftNum = nums[startIdx]
                    freqMap[leftNum] -= 1
                    if freqMap[leftNum] == 0:
                        uniqElems -= 1
                    startIdx += 1
                totalCount += endIdx - startIdx + 1
            return totalCount

        n = len(nums)
        totalSubs = n * (n + 1) // 2
        medianIdx = (totalSubs + 1) // 2
        leftBound, rightBound = 1, n

        while leftBound < rightBound:
            midpoint = leftBound + (rightBound - leftBound) // 2
            if countLessOrEqual(midpoint) < medianIdx:
                leftBound = midpoint + 1
            else:
                rightBound = midpoint

        return leftBound