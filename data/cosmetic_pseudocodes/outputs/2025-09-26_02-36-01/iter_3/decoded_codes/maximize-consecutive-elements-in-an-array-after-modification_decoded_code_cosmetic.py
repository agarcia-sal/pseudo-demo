class Solution:
    def maxSelectedElements(self, nums):
        maximumCount = 0
        records = {}
        sortedValues = sorted(nums)

        index = 0
        while index < len(sortedValues):
            currentNumber = sortedValues[index]

            prevVal = records.get(currentNumber - 1, 0)
            plusOneVal = records.get(currentNumber + 1, 0)

            records[currentNumber + 1] = plusOneVal + 1
            records[currentNumber] = prevVal + 1

            currentMax2 = records[currentNumber]
            currentMax3 = records[currentNumber + 1]

            if currentMax2 > maximumCount:
                maximumCount = currentMax2
            if currentMax3 > maximumCount:
                maximumCount = currentMax3

            index += 1

        return maximumCount