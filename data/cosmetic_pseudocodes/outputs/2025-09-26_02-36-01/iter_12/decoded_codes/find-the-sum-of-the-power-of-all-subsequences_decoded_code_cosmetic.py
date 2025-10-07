class Solution:
    def sumOfPower(self, nums: list[int], k: int) -> int:
        ConstantMod = 10**9 + 7
        lengthVal = len(nums)

        def CloneList(size1: int, size2: int) -> list[list[int]]:
            res = []
            outerCounter = 0
            while outerCounter < size1 + 1:
                innerList = []
                innerCounter = 0
                while innerCounter < size2 + 1:
                    innerList.append(0)
                    innerCounter += 1
                res.append(innerList)
                outerCounter += 1
            return res

        matrixDp = CloneList(lengthVal, k)
        matrixDp[0][0] = 1

        def AddModulo(a: int, b: int) -> int:
            return (a + b) % ConstantMod

        iIndex = 1
        while iIndex <= lengthVal:
            jIndex = 0
            while jIndex <= k:
                tempVal = matrixDp[iIndex - 1][jIndex]
                if jIndex >= nums[iIndex - 1]:
                    tempVal = AddModulo(tempVal, matrixDp[iIndex - 1][jIndex - nums[iIndex - 1]])
                matrixDp[iIndex][jIndex] = tempVal
                jIndex += 1
            iIndex += 1

        def BitIsSet(numValue: int, posValue: int) -> bool:
            return ((numValue >> posValue) & 1) == 1

        finalPower = 0
        upperLimit = (1 << lengthVal) - 1

        maskIndex = 1
        while maskIndex <= upperLimit:
            sumCurrent = 0
            bitsCount = 0
            bitPos = 0
            while bitPos < lengthVal:
                if BitIsSet(maskIndex, bitPos):
                    sumCurrent += nums[bitPos]
                    bitsCount += 1
                bitPos += 1

            if sumCurrent == k:
                additionVal = pow(2, lengthVal - bitsCount, ConstantMod)
                finalPower = (finalPower + additionVal) % ConstantMod

            maskIndex += 1

        return finalPower