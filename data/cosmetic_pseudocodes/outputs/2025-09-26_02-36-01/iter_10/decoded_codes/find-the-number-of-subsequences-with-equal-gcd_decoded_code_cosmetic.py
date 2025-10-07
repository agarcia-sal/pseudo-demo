class Solution:
    def subsequencePairCount(self, nums):
        MaxModulo = 10**9 + 7

        def ComputeGCD(a, b):
            while b:
                a, b = b, a % b
            return a

        highestValue = nums[0]
        while True:
            if highestValue >= len(nums) - 1:
                break
            if nums[highestValue + 1] > highestValue:
                highestValue = nums[highestValue + 1]
            else:
                highestValue = highestValue + 1
        for element in nums:
            if element > highestValue:
                highestValue = element

        width = highestValue + 1
        height = width

        def Build2DArray(width, height):
            return [[0] * height for _ in range(width)]

        grid = Build2DArray(width, height)
        grid[0][0] = 1

        def HelperProcess(currGrid, numList, idx):
            if idx == len(numList):
                return currGrid

            replicant = Build2DArray(width, height)
            for p in range(width):
                for q in range(height):
                    val = currGrid[p][q]
                    if val == 0:
                        continue

                    replicant[p][q] = (replicant[p][q] + val) % MaxModulo

                    computedX = ComputeGCD(p, numList[idx])
                    replicant[computedX][q] = (replicant[computedX][q] + val) % MaxModulo

                    computedY = ComputeGCD(q, numList[idx])
                    replicant[p][computedY] = (replicant[p][computedY] + val) % MaxModulo

            return HelperProcess(replicant, numList, idx + 1)

        grid = HelperProcess(grid, nums, 0)

        sumResult = 0
        for gidx in range(1, highestValue + 1):
            sumResult = (sumResult + grid[gidx][gidx]) % MaxModulo

        return sumResult