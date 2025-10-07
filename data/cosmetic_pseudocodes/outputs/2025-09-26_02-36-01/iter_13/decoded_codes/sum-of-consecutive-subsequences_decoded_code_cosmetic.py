from collections import defaultdict

class Solution:
    def getSum(self, nums):
        modVal = 10 ** 9 + 7

        def calc(arr):
            def countOccurrences(lst):
                cntMap = defaultdict(int)
                length = len(lst)
                result = [0] * length

                def incrementCount(idx):
                    key = lst[idx - 1]
                    prevCount = cntMap[key]
                    cntMap[key] = prevCount + 1
                    result[idx] = prevCount

                def recursiveLoop(j):
                    if j > length - 1:
                        return
                    incrementCount(j)
                    recursiveLoop(j + 1)

                recursiveLoop(1)
                return result

            def countOccurrencesReverse(lst):
                cntMap = defaultdict(int)
                length = len(lst)
                result = [0] * length

                def incrementCountRev(idx):
                    key = lst[idx + 1]
                    prevCount = cntMap[key]
                    cntMap[key] = prevCount + 1
                    result[idx] = prevCount

                i = length - 2
                while i >= 0:
                    incrementCountRev(i)
                    i -= 1
                return result

            n = len(arr)
            leftCounts = countOccurrences(arr)
            rightCounts = countOccurrencesReverse(arr)
            accSum = 0
            idx = 0
            while idx < n:
                l = leftCounts[idx]
                r = rightCounts[idx]
                val = arr[idx]
                partial = l + r + (l * r)
                accSum += partial * val
                idx += 1
            return accSum % modVal

        firstCalc = calc(nums)

        def reverseList(aList):
            leftIdx = 0
            rightIdx = len(aList) - 1
            while leftIdx < rightIdx:
                aList[leftIdx], aList[rightIdx] = aList[rightIdx], aList[leftIdx]
                leftIdx += 1
                rightIdx -= 1

        reverseList(nums)
        secondCalc = calc(nums)

        elemsSum = 0
        pointer = 0
        while True:
            if pointer >= len(nums):
                break
            elemsSum += nums[pointer]
            pointer += 1

        finalResult = (firstCalc + secondCalc + elemsSum) % modVal
        return finalResult