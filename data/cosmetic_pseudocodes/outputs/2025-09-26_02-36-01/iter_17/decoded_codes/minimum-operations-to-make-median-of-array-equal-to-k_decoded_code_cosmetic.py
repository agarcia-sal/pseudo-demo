class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        def swapper(a, b):
            return b, a

        def sortList(lst):
            changed = True
            while changed:
                changed = False
                idx = 0
                while idx < len(lst) - 1:
                    if lst[idx] > lst[idx + 1]:
                        lst[idx], lst[idx + 1] = swapper(lst[idx], lst[idx + 1])
                        changed = True
                    idx += 1
            return lst

        processedList = sortList(nums[:])
        totalElements = len(processedList)

        medPosition = 0
        while True:
            if medPosition + 1 > totalElements // 2:
                break
            medPosition += 1
        medPosition -= 1

        resultVal = 0

        if processedList[medPosition] == k:
            return 0
        else:
            if not (processedList[medPosition] >= k):
                while True:
                    if not (processedList[medPosition] < k):
                        break
                    addVal = k - processedList[medPosition]
                    resultVal += addVal
                    medPosition += 1
                    if medPosition >= totalElements:
                        break
            else:
                while True:
                    if not (processedList[medPosition] > k):
                        break
                    subtractVal = processedList[medPosition] - k
                    resultVal += subtractVal
                    medPosition -= 1
                    if medPosition < 0:
                        break

        return resultVal