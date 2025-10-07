class Solution:
    def maxSelectedElements(self, nums):
        result = 0
        table = {}
        sortedList = sorted(nums)
        idx = 0
        while idx < len(sortedList):
            currentVal = sortedList[idx]

            nextValCount = 1
            if currentVal in table:
                nextValCount = table[currentVal] + 1
            table[currentVal + 1] = nextValCount

            prevValCount = 1
            if (currentVal - 1) in table:
                prevValCount = table[currentVal - 1] + 1
            table[currentVal] = prevValCount

            tempMax = result
            if tempMax < table[currentVal]:
                tempMax = table[currentVal]
            if tempMax < table[currentVal + 1]:
                tempMax = table[currentVal + 1]
            result = tempMax

            idx += 1

        return result