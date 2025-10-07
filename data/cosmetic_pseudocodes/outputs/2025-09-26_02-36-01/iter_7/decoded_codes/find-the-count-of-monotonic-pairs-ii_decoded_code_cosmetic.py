class Solution:
    def countOfPairs(self, nums):
        MODULUS = 10**9 + 7
        totalElements = len(nums)
        highestValue = nums[0]
        indexCounter = 1
        while indexCounter < totalElements:
            if highestValue < nums[indexCounter]:
                highestValue = nums[indexCounter]
            indexCounter += 1

        def zero3dArray(dim1, dim2, dim3):
            outerList = []
            x = 0
            while x < dim1:
                middleList = []
                y = 0
                while y < dim2:
                    innerList = []
                    z = 0
                    while z < dim3:
                        innerList.append(0)
                        z += 1
                    middleList.append(innerList)
                    y += 1
                outerList.append(middleList)
                x += 1
            return outerList

        dpTable = zero3dArray(totalElements + 1, highestValue + 1, highestValue + 1)

        jIndex = 0
        firstNum = nums[0]
        while True:
            if jIndex > firstNum:
                break
            complementaryIndex = firstNum - jIndex
            dpTable[1][jIndex][complementaryIndex] = 1
            jIndex += 1

        iIndex = 2
        while iIndex <= totalElements:
            currentNum = nums[iIndex - 1]
            jSubIndex = 0
            while jSubIndex <= currentNum:
                kSubIndex = 0
                while kSubIndex <= currentNum:
                    sumCheck = jSubIndex + kSubIndex
                    if sumCheck == currentNum:
                        prevJ = 0
                        while prevJ <= jSubIndex:
                            prevK = kSubIndex
                            while prevK <= highestValue:
                                dpTable[iIndex][jSubIndex][kSubIndex] += dpTable[iIndex - 1][prevJ][prevK]
                                if dpTable[iIndex][jSubIndex][kSubIndex] >= MODULUS:
                                    dpTable[iIndex][jSubIndex][kSubIndex] -= MODULUS
                                prevK += 1
                            prevJ += 1
                    kSubIndex += 1
                jSubIndex += 1
            iIndex += 1

        accumulationVariable = 0
        outerJ = 0
        while outerJ <= highestValue:
            innerK = 0
            while innerK <= highestValue:
                accumulationVariable += dpTable[totalElements][outerJ][innerK]
                if accumulationVariable >= MODULUS:
                    accumulationVariable -= MODULUS
                innerK += 1
            outerJ += 1

        return accumulationVariable