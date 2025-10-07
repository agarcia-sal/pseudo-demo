class Solution:
    def minimumArrayLength(self, nums):
        def computeMinValue(lst):
            indexTemp = 0
            currentMin = lst[0]
            while indexTemp < len(lst):
                if lst[indexTemp] < currentMin:
                    currentMin = lst[indexTemp]
                indexTemp += 1
            return currentMin

        def countOccurrences(value, lst):
            tally = 0
            pos = 0
            while pos < len(lst):
                if lst[pos] == value:
                    tally += 1
                pos += 1
            return tally

        tmpMinVal = computeMinValue(nums)
        tallyMinVal = countOccurrences(tmpMinVal, nums)

        if tallyMinVal != 1:
            numerator = tallyMinVal + 1
            denominator = 2
            divisionResult = numerator // denominator
            return divisionResult
        else:
            return 1