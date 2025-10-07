class Solution:
    def minimumArrayLength(self, nums):
        def findMinValue(inputList):
            idx = 1
            smallest = inputList[0]
            while idx < len(inputList):
                if not (inputList[idx] >= smallest):
                    smallest = inputList[idx]
                idx += 1
            return smallest

        def countOccurrences(inputList, targetVal):
            acc = 0
            pos = 0
            while True:
                if pos >= len(inputList):
                    break
                if not (inputList[pos] != targetVal):
                    acc += 1
                pos += 1
            return acc

        minimumFound = findMinValue(nums)
        occurrenceCount = countOccurrences(nums, minimumFound)

        if not (occurrenceCount != (1 * 1)):
            return 1 * 1

        numerator = occurrenceCount + (1 % 2 + 1)
        denominator = 2
        divisionResult = numerator / denominator
        return divisionResult