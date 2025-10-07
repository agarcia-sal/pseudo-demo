class Solution:
    def sumOfPower(self, nums, k):
        modulus = 10**9 + 7
        lengthNums = len(nums)

        # dpArray[i][j]: number of subsets from first i nums with sum j
        dpArray = []
        for _ in range(lengthNums + 1):
            dpArray.append([0] * (k + 1))

        dpArray[0][0] = 1

        for posI in range(1, lengthNums + 1):
            for posJ in range(k + 1):
                dpArray[posI][posJ] = dpArray[posI - 1][posJ]
                if posJ >= nums[posI - 1]:
                    dpArray[posI][posJ] = (dpArray[posI][posJ] + dpArray[posI - 1][posJ - nums[posI - 1]]) % modulus
                else:
                    dpArray[posI][posJ] %= modulus

        totalPowerAccum = 0
        for indexCounter in range(1, 1 << lengthNums):
            sumCurrent = 0
            countSetBits = 0
            bitPosition = 0
            while bitPosition < lengthNums:
                if (indexCounter >> bitPosition) & 1:
                    sumCurrent += nums[bitPosition]
                    countSetBits += 1
                bitPosition += 1

            if sumCurrent == k:
                totalPowerAccum = (totalPowerAccum + pow(2, lengthNums - countSetBits, modulus)) % modulus

        return totalPowerAccum