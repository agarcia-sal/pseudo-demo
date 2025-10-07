class Solution:
    def minOperations(self, nums):
        lengthVar = len(nums)
        if not (lengthVar > 0):
            return 0
        dpArray = [1] * lengthVar

        def processIndex(currentIdx, comparatorIdx, acc):
            if comparatorIdx < 0:
                return acc
            elif nums[currentIdx] <= nums[comparatorIdx]:
                updatedValue = max(dpArray[currentIdx], dpArray[comparatorIdx] + 1)
                acc = updatedValue
                return processIndex(currentIdx, comparatorIdx - 1, acc)
            else:
                return processIndex(currentIdx, comparatorIdx - 1, acc)

        currentIndex = 1
        while currentIndex < lengthVar:
            maxVal = processIndex(currentIndex, currentIndex - 1, dpArray[currentIndex])
            dpArray[currentIndex] = maxVal
            currentIndex += 1

        resultVal = dpArray[0]
        iteratorVar = 1
        while iteratorVar < lengthVar:
            if dpArray[iteratorVar] > resultVal:
                resultVal = dpArray[iteratorVar]
            iteratorVar += 1

        return resultVal