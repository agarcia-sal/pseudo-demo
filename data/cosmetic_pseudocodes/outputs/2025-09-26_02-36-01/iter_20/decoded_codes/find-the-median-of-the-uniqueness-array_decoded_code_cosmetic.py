from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(x):
            def incrementAt(k, mapRef):
                mapRef[k] = mapRef.get(k, 0) + 1

            def decrementAt(k, mapRef):
                mapRef[k] -= 1

            z = 0
            w = 0
            dMap = defaultdict(int)
            v = 0
            totalCount = 0

            while w < len(nums):
                if dMap[nums[w]] == 0:
                    v += 1
                incrementAt(nums[w], dMap)
                while v > x:
                    decrementAt(nums[z], dMap)
                    if dMap[nums[z]] == 0:
                        v -= 1
                    z += 1
                countTemp = w - z + 1
                totalCount += countTemp
                w += 1
            return totalCount

        k = len(nums)
        totalSubs = k * (k + 1) // 2
        medianIdx = (totalSubs + 1) // 2

        a, b = 1, k

        def halfDivide(low, high):
            return low + (high - low) // 2

        while a < b:
            c = halfDivide(a, b)
            if countLessOrEqual(c) < medianIdx:
                a = c + 1
            else:
                b = c
        return a