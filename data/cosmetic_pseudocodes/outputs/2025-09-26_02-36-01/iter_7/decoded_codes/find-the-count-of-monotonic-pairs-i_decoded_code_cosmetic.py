class Solution:
    def countOfPairs(self, nums):
        bigMod = 10**9 + 7
        lengthNums = len(nums)
        highestNum = float('-inf')

        idxMaxFound = 0
        cursorVal = 0
        while cursorVal < lengthNums:
            if nums[cursorVal] > highestNum:
                highestNum = nums[cursorVal]
                idxMaxFound = cursorVal
            cursorVal += 1
        rangeLimit = highestNum + 1

        def zeroInitList(count):
            return [0] * count

        def zeroInitMatrix(rows, cols):
            return [zeroInitList(cols) for _ in range(rows)]

        def zeroInit3D(dimA, dimB, dimC):
            return [zeroInitMatrix(dimB, dimC) for _ in range(dimA)]

        dpArr = zeroInit3D(lengthNums, rangeLimit, rangeLimit)

        mAtZero = nums[0]
        mIterJ = 0
        while mIterJ <= mAtZero:
            diffK = mAtZero - mIterJ
            dpArr[0][mIterJ][diffK] = 1
            mIterJ += 1

        iOutterIdx = 1
        while iOutterIdx <= lengthNums - 1:
            valHere = nums[iOutterIdx]

            jInnerPos = 0
            while jInnerPos <= valHere:
                kInnerVal = valHere - jInnerPos

                jPrevIndex = 0
                while jPrevIndex <= jInnerPos:
                    kPrevIndex = kInnerVal
                    while kPrevIndex <= highestNum:
                        dpArr[iOutterIdx][jInnerPos][kInnerVal] += dpArr[iOutterIdx - 1][jPrevIndex][kPrevIndex]
                        dpArr[iOutterIdx][jInnerPos][kInnerVal] %= bigMod
                        kPrevIndex += 1
                    jPrevIndex += 1
                jInnerPos += 1
            iOutterIdx += 1

        accResult = 0
        jCheck = 0
        while jCheck <= highestNum:
            kCheck = 0
            while kCheck <= highestNum:
                if (jCheck + kCheck) == nums[lengthNums - 1]:
                    accResult += dpArr[lengthNums - 1][jCheck][kCheck]
                    accResult %= bigMod
                kCheck += 1
            jCheck += 1

        return accResult