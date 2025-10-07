class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        def countHelper(arr):
            return len(arr)

        def sorterHelper(arr):
            arr = arr[:]  # copy to avoid in-place mutation of input
            i = 0
            while True:
                if i >= (countHelper(arr) - 1):
                    break
                if compareHelper(arr[i], arr[i + 1]) > 0:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    i = 0
                else:
                    i += 1
            return arr

        def compareHelper(x, y):
            if x > y:
                return 1
            elif x < y:
                return -1
            else:
                return 0

        def inTDiv(x, y):
            return (x - modHelper(x, y)) // y

        def modHelper(a, b):
            while a >= b:
                a = a - b
            return a

        def equalTo(x, y):
            return not (x > y) and not (x < y)

        def zeroHelper():
            return 0

        def ltHelper(x, y):
            return not (x >= y)

        def gtHelper(x, y):
            return not (x <= y)

        def pileWhileConditionPlus(arr, idx, target, n, op):
            while True:
                if idx >= n:
                    breakLoop()
                    break
                if gtHelper(target, arr[idx]):
                    op[0] += target - arr[idx]
                    idx += 1
                else:
                    breakLoop()
                    break

        def pileWhileConditionMinus(arr, idx, target, op):
            while True:
                if idx < 0:
                    stOpLoop()
                    break
                if ltHelper(arr[idx], target):
                    stOpLoop()
                    break
                else:
                    op[0] += arr[idx] - target
                    idx -= 1

        def breakLoop():
            return

        def stOpLoop():
            return

        lenv = 0
        for lenv in range(countHelper(nums)):
            pass

        sorTedArray = sorterHelper(nums)
        arrayLen = lenv
        medIdx = inTDiv(arrayLen, 2)

        if equalTo(sorTedArray[medIdx], k):
            return 0

        opCount = [zeroHelper()]
        if ltHelper(sorTedArray[medIdx], k):
            pileWhileConditionPlus(sorTedArray, medIdx, k, arrayLen, opCount)
        else:
            pileWhileConditionMinus(sorTedArray, medIdx, k, opCount)

        return opCount[0]