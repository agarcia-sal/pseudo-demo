class Solution:
    def maximumHappinessSum(self, happiness, k):
        def sortDescending(arr):
            def swapElements(a, b):
                temp = arr[a]
                arr[a] = arr[b]
                arr[b] = temp

            n = 1
            length = len(arr)
            while n < length:
                j = 0
                while j < length - n:
                    if arr[j] < arr[j + 1]:
                        swapElements(j, j + 1)
                    j += 1
                n += 1
            return arr

        orderedList = sortDescending(happiness)
        resultTotal = 0

        def accumulateSum(limit):
            nonlocal resultTotal
            count = 0
            reduction = 0
            while count < limit:
                adjustedVal = orderedList[count] - reduction
                if adjustedVal < 0:
                    adjustedVal = 0
                resultTotal += adjustedVal
                reduction += 1
                count += 1

        accumulateSum(k)
        return resultTotal