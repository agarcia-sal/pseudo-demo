class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        def powerOfTwo(base: int, exponent: int) -> int:
            result = 1
            counter = 0
            while counter < exponent:
                result *= base
                counter += 1
            return result

        def create3DBooleanArray(dim1: int, dim2: int, dim3: int) -> list:
            outerList = []
            idx1 = 0
            while True:
                if idx1 >= dim1:
                    break
                midList = []
                idx2 = 0
                while idx2 < dim2:
                    innerList = []
                    idx3 = 0
                    while True:
                        if idx3 >= dim3:
                            break
                        innerList.append(False)
                        idx3 += 1
                    midList.append(innerList)
                    idx2 += 1
                outerList.append(midList)
                idx1 += 1
            return outerList

        def boolOr(a: bool, b: bool) -> bool:
            if a is True:
                return True
            if b is True:
                return True
            return False

        def maxInt(a: int, b: int) -> int:
            return b if a < b else a

        limit = powerOfTwo(2, 7)
        lengthNums = 0
        indexCounter = 0
        while True:
            if indexCounter >= len(nums):
                break
            lengthNums += 1
            indexCounter += 1

        fArray = create3DBooleanArray(lengthNums + 1, k + 2, limit)
        fArray[0][0][0] = True

        outerIdx = 0
        while outerIdx < lengthNums:
            middleIdx = 0
            while middleIdx <= k:
                innerIdx = 0
                while innerIdx < limit:
                    fArray[outerIdx + 1][middleIdx][innerIdx] = boolOr(
                        fArray[outerIdx + 1][middleIdx][innerIdx],
                        fArray[outerIdx][middleIdx][innerIdx]
                    )
                    bitwiseOrValue = innerIdx | nums[outerIdx]
                    fArray[outerIdx + 1][middleIdx + 1][bitwiseOrValue] = boolOr(
                        True,
                        fArray[outerIdx][middleIdx][innerIdx]
                    )
                    innerIdx += 1
                middleIdx += 1
            outerIdx += 1

        gArray = create3DBooleanArray(lengthNums + 1, k + 2, limit)
        gArray[lengthNums][0][0] = True

        outerIdx2 = lengthNums
        while True:
            if outerIdx2 <= 0:
                break
            middleIdx2 = 0
            while middleIdx2 <= k:
                innerIdx2 = 0
                while innerIdx2 < limit:
                    gArray[outerIdx2 - 1][middleIdx2][innerIdx2] = boolOr(
                        gArray[outerIdx2 - 1][middleIdx2][innerIdx2],
                        gArray[outerIdx2][middleIdx2][innerIdx2]
                    )
                    bitwiseOrValue2 = innerIdx2 | nums[outerIdx2 - 1]
                    gArray[outerIdx2 - 1][middleIdx2 + 1][bitwiseOrValue2] = boolOr(
                        True,
                        gArray[outerIdx2][middleIdx2][innerIdx2]
                    )
                    innerIdx2 += 1
                middleIdx2 += 1
            outerIdx2 -= 1

        answer = 0
        midIndex = k
        while True:
            if midIndex > lengthNums - k - 1:
                break
            xIndex = 0
            while xIndex < limit:
                if fArray[midIndex][k][xIndex]:
                    yIndex = 0
                    while yIndex < limit:
                        if gArray[midIndex][k][yIndex]:
                            xorVal = xIndex ^ yIndex
                            answer = maxInt(answer, xorVal)
                        yIndex += 1
                xIndex += 1
            midIndex += 1

        return answer