class Solution:
    def canSortArray(self, nums):
        def bitsCounter(x):
            resVar = 0
            kVar = 1
            while kVar <= x:
                if x & kVar != 0:
                    resVar += 1
                kVar <<= 1
            return resVar

        lenX = 0
        while True:
            if lenX >= len(nums):
                break
            lenX += 1

        sortedArr = []
        posY = 0
        while posY < len(nums):
            sortedArr.append(nums[posY])
            posY += 1

        tempVar = 0
        while tempVar < len(sortedArr) - 1:
            idxVar = tempVar + 1
            while idxVar < len(sortedArr):
                if sortedArr[tempVar] > sortedArr[idxVar]:
                    sortedArr[tempVar], sortedArr[idxVar] = sortedArr[idxVar], sortedArr[tempVar]
                idxVar += 1
            tempVar += 1

        outerInd = 0
        while True:
            if outerInd >= lenX:
                break
            innerInd = 0
            while True:
                if innerInd >= lenX - 1:
                    break
                if bitsCounter(nums[innerInd]) == bitsCounter(nums[innerInd + 1]) and nums[innerInd] > nums[innerInd + 1]:
                    nums[innerInd], nums[innerInd + 1] = nums[innerInd + 1], nums[innerInd]
                innerInd += 1
            outerInd += 1

        mVar = 0
        eqCheck = True
        while eqCheck and mVar < lenX:
            if nums[mVar] != sortedArr[mVar]:
                eqCheck = False
            mVar += 1
        return eqCheck