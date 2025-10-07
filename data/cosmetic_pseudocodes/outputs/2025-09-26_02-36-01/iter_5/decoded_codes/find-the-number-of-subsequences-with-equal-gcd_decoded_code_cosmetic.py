class Solution:
    def subsequencePairCount(self, nums):
        moduloVal = 10**9 + 7
        upperBound = nums[0]
        idx1 = 1
        while idx1 < len(nums):
            if nums[idx1] > upperBound:
                upperBound = nums[idx1]
            idx1 += 1

        dpArray = [[0] * (upperBound + 1) for _ in range(upperBound + 1)]
        dpArray[0][0] = 1

        def gcdHelper(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def processIndex(i):
            nonlocal dpArray
            if i == len(nums):
                return
            currentNum = nums[i]
            updatedDp = [[0] * (upperBound + 1) for _ in range(upperBound + 1)]

            for idxX in range(upperBound + 1):
                for idxY in range(upperBound + 1):
                    baseVal = dpArray[idxX][idxY]

                    # continue without adding currentNum
                    sumVal1 = updatedDp[idxX][idxY] + baseVal
                    updatedDp[idxX][idxY] = sumVal1 % moduloVal

                    # gcd with idxX
                    gX = gcdHelper(idxX, currentNum)
                    sumVal2 = updatedDp[gX][idxY] + baseVal
                    updatedDp[gX][idxY] = sumVal2 % moduloVal

                    # gcd with idxY
                    gY = gcdHelper(idxY, currentNum)
                    sumVal3 = updatedDp[idxX][gY] + baseVal
                    updatedDp[idxX][gY] = sumVal3 % moduloVal

            dpArray = updatedDp
            processIndex(i + 1)

        processIndex(0)

        accumulator = 0
        counter = 1
        while counter <= upperBound:
            accumulator = (accumulator + dpArray[counter][counter]) % moduloVal
            counter += 1

        finalResult = accumulator
        return finalResult