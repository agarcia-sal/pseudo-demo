class Solution:
    def canSortArray(self, nums):
        def bitCount(x):
            def countOnes(val, acc):
                if val == 0:
                    return acc
                else:
                    return countOnes(val >> 1, acc + (val & 1))
            return countOnes(x, 0)

        lenNums = len(nums)
        sortedCopy = [nums[i] for i in range(lenNums)]
        sortedCopy2 = [sortedCopy[x] for x in range(lenNums)]

        def comparator(a, b):
            return a - b

        def simpleSort(arr):
            def bubbleRecur(i, j, arrInner):
                if i >= len(arrInner):
                    return arrInner
                if j >= len(arrInner) - 1:
                    return bubbleRecur(i + 1, 0, arrInner)

                leftVal, rightVal = arrInner[j], arrInner[j + 1]
                if comparator(leftVal, rightVal) > 0:
                    temporary = arrInner[j]
                    arrInner[j] = arrInner[j + 1]
                    arrInner[j + 1] = temporary
                return bubbleRecur(i, j + 1, arrInner)
            return bubbleRecur(0, 0, arr)

        sortedCopy2 = simpleSort(sortedCopy2)

        def swapAdjacentByBitCount(arr, limit, outerInd):
            if outerInd >= limit:
                return
            def innerSwap(j, limitInner, arrInner):
                if j >= limitInner:
                    return
                left, right = arrInner[j], arrInner[j + 1]
                if bitCount(left) == bitCount(right) and left > right:
                    tempHolder = arrInner[j]
                    arrInner[j] = arrInner[j + 1]
                    arrInner[j + 1] = tempHolder
                innerSwap(j + 1, limitInner, arrInner)
            innerSwap(0, limit - 1, arr)
            swapAdjacentByBitCount(arr, limit, outerInd + 1)

        swapAdjacentByBitCount(nums, lenNums, 0)

        def arraysEqual(a1, a2, index):
            if index == len(a1):
                return True
            if a1[index] != a2[index]:
                return False
            return arraysEqual(a1, a2, index + 1)

        return arraysEqual(nums, sortedCopy2, 0)