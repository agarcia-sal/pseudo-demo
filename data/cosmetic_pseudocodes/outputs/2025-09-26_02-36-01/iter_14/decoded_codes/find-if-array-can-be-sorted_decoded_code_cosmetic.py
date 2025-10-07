class Solution:
    def canSortArray(self, nums):
        def bitCount(k):
            result = 0
            while k != 0:
                result += k & 1
                k >>= 1
            return result

        lengthVal = 0
        while lengthVal < len(nums):
            lengthVal += 1

        sortedCopy = []
        for indexVar in range(lengthVal):
            sortedCopy.append(nums[indexVar])

        def customSort(arr):
            def innerSwapCheck(x):
                return bitCount(arr[x]) > bitCount(arr[x + 1])

            outerIdx = 0
            while True:
                innerIdx = 0
                swapped = False
                while innerIdx < lengthVal - 1:
                    if bitCount(arr[innerIdx]) == bitCount(arr[innerIdx + 1]) and innerSwapCheck(innerIdx):
                        arr[innerIdx], arr[innerIdx + 1] = arr[innerIdx + 1], arr[innerIdx]
                        swapped = True
                    innerIdx += 1
                outerIdx += 1
                if outerIdx > lengthVal or not swapped:
                    break

        customSort(nums)

        def equalCheck():
            i = 0
            while i < lengthVal:
                if nums[i] != sortedCopy[i]:
                    return False
                i += 1
            return True

        return not equalCheck()