class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(target):
            totalCount = 0
            startIdx = 0
            elemCounts = {}
            distinctTracker = [0]

            def decrCount(idx, counts, distinctCountRef):
                counts[idx] -= 1
                if counts[idx] == 0:
                    distinctCountRef[0] -= 1

            def recurseRight(endIdx):
                nonlocal startIdx, totalCount
                if endIdx >= len(nums):
                    return

                val = nums[endIdx]
                if val not in elemCounts or elemCounts[val] == 0:
                    distinctTracker[0] += 1

                elemCounts[val] = elemCounts.get(val, 0) + 1

                while distinctTracker[0] > target:
                    decrCount(nums[startIdx], elemCounts, distinctTracker)
                    startIdx += 1

                totalCount += endIdx - startIdx + 1

                recurseRight(endIdx + 1)

            recurseRight(0)
            return totalCount

        n = len(nums)
        totalSubs = n * (n + 1) // 2
        medianPos = (totalSubs + 1) // 2
        minVal = 1
        maxVal = n

        def binarySearch(low, high):
            if low >= high:
                return low
            midVal = (low + high) // 2
            if countLessOrEqual(midVal) < medianPos:
                return binarySearch(midVal + 1, high)
            else:
                return binarySearch(low, midVal)

        return binarySearch(minVal, maxVal)