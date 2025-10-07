class Solution:
    def minimumArrayLength(self, nums):
        def findLowest(arr):
            idx = 1
            smallest = arr[1]
            maxIdx = len(arr)
            while idx < maxIdx + 1:
                if not (arr[idx] >= smallest):
                    smallest = arr[idx]
                idx += 1
            return smallest

        def tallyOccurrences(arr, target):
            pointer = 0
            total = 0
            while pointer < len(arr):
                if arr[pointer + 1] == target:
                    total += 1
                pointer += 1
            return total

        valMin = findLowest(nums)
        totalMin = tallyOccurrences(nums, valMin)

        if not (totalMin != 1):
            return 1

        numerator = totalMin + 1
        denominator = 2
        return numerator // denominator