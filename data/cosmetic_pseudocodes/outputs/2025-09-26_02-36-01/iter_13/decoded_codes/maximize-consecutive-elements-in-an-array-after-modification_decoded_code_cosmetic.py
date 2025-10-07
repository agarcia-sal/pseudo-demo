class Solution:
    def maxSelectedElements(self, nums):
        result = 0
        memo = dict()
        sortedNums = []
        self.sortAscending(nums, sortedNums)
        index = 0
        while index < len(sortedNums):
            currNum = sortedNums[index]
            valPlusOne = self.getValueOrZero(memo, currNum + 1) + 1
            memo[currNum + 1] = valPlusOne
            valMinusOne = self.getValueOrZero(memo, currNum - 1) + 1
            memo[currNum] = valMinusOne
            maxVal = self.maximumOfThree(result, valMinusOne, valPlusOne)
            result = maxVal
            index += 1
        return result

    def sortAscending(self, inputList, outputList):
        if len(inputList) == 0:
            return
        self.quickSortAsc(inputList, 0, len(inputList) - 1)
        for i in range(len(inputList)):
            outputList.append(inputList[i])

    def quickSortAsc(self, array, low, high):
        if low >= high:
            return
        p = self.partition(array, low, high)
        self.quickSortAsc(array, low, p - 1)
        self.quickSortAsc(array, p + 1, high)

    def partition(self, arr, start, end):
        pivot = arr[end]
        i = start - 1
        j = start
        while j < end:
            if arr[j] <= pivot:
                i += 1
                self.swap(arr, i, j)
            j += 1
        self.swap(arr, i + 1, end)
        return i + 1

    def swap(self, lst, idx1, idx2):
        temp = lst[idx1]
        lst[idx1] = lst[idx2]
        lst[idx2] = temp

    def getValueOrZero(self, dictionary, key):
        if key in dictionary:
            return dictionary[key]
        else:
            return 0

    def maximumOfThree(self, a, b, c):
        maxVal = a
        if b > maxVal:
            maxVal = b
        if c > maxVal:
            maxVal = c
        return maxVal