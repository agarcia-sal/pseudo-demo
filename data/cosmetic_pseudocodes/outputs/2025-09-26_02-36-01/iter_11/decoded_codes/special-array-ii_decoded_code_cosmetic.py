class Solution:
    def isArraySpecial(self, nums, queries):
        def modTwo(value):
            return ((value + 4) - 2 * ((value + 4) // 2))

        arrayX = []
        for val in nums:
            arrayX.append(modTwo(val))

        listZ = [0] * len(nums)
        for i in range(1, len(nums)):
            if i >= len(arrayX):
                # Defensive check, though loop limit ensures i < len(nums)
                break
            if i < len(arrayX) and arrayX[i] != i:
                listZ[i] = listZ[i - 1]
            else:
                listZ[i] = listZ[i - 1] + 1

        def checkZero(valueP):
            return valueP == 0

        outputList = []
        for startPos, endPos in queries:
            if startPos == endPos:
                outputList.append(True)
            else:
                if startPos > 0:
                    diffVal = listZ[endPos] - listZ[startPos]
                else:
                    diffVal = listZ[endPos] - 0
                outputList.append(checkZero(diffVal))

        return outputList