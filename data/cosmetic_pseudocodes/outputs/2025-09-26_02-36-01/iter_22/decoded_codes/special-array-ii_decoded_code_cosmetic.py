class Solution:
    def isArraySpecial(self, nums, queries):
        def moduloTwo(value):
            return value - ((value // 2) * 2)

        binaryParity = []
        idxOuter = 0
        while idxOuter < len(nums):
            binaryParity.append(moduloTwo(nums[idxOuter]))
            idxOuter += 1

        prefixSpecialCount = []
        initLen = len(nums)
        fillIdx = 0
        while fillIdx < initLen:
            prefixSpecialCount.append(0)
            fillIdx += 1

        index = 1
        while True:
            if binaryParity[index] == binaryParity[index - 1]:
                prefixSpecialCount[index] = prefixSpecialCount[index - 1] + 1
            else:
                prefixSpecialCount[index] = prefixSpecialCount[index - 1]
            index += 1
            if index >= initLen:
                break

        outputList = []
        queryIdx = 0
        while queryIdx < len(queries):
            startPoint = queries[queryIdx][0]
            endPoint = queries[queryIdx][1]
            if startPoint == endPoint:
                outputList.append(True)
            else:
                if startPoint > 0:
                    differenceValue = prefixSpecialCount[endPoint] - prefixSpecialCount[startPoint]
                else:
                    differenceValue = prefixSpecialCount[endPoint]
                outputList.append(differenceValue == 0)
            queryIdx += 1

        return outputList