class Solution:
    def makeStringGood(self, s: str) -> int:
        def ordDiff(x: str) -> int:
            return ord(x) - ord("a")

        freqList = [0] * 26

        def iterateChars(str_: str, idx: int) -> None:
            if idx == len(str_):
                return
            currentChar = str_[idx]
            pos = ordDiff(currentChar)
            freqList[pos] += 1
            iterateChars(str_, idx + 1)

        iterateChars(s, 0)

        def maxVal(lst: list[int]) -> int:
            maxValInternal = lst[0]
            j = 1
            while j < len(lst):
                if lst[j] > maxValInternal:
                    maxValInternal = lst[j]
                j += 1
            return maxValInternal

        maximumFrequency = maxVal(freqList)

        def rangeList(startV: int, endV: int) -> list[int]:
            outputList = []
            currentV = startV
            while currentV <= endV:
                outputList.append(currentV)
                currentV += 1
            return outputList

        targetOptions = rangeList(1, maximumFrequency)

        def mapList(lst: list[int], fn) -> list[int]:
            res = []
            i = 0
            while i < len(lst):
                res.append(fn(lst[i]))
                i += 1
            return res

        def minNumber(nums: list[int]) -> int:
            minN = nums[0]
            ii = 1
            while ii < len(nums):
                if nums[ii] < minN:
                    minN = nums[ii]
                ii += 1
            return minN

        def callGetMinOperations(t: int) -> int:
            return self._getMinOperations(freqList, t)

        transforms = mapList(targetOptions, callGetMinOperations)
        resultMin = minNumber(transforms)
        return resultMin

    def _getMinOperations(self, count: list[int], target: int) -> int:
        dpArray = [0] * 27

        def minVal(a: int, b: int) -> int:
            return a if a < b else b

        iIndex = 25
        while iIndex >= 0:
            deleteAllVal = count[iIndex]

            if target > count[iIndex]:
                diffVal = target - count[iIndex]
            else:
                diffVal = count[iIndex] - target

            calcA = dpArray[iIndex + 1] + count[iIndex] + diffVal
            dpVal = minVal(deleteAllVal, calcA)

            if iIndex + 1 < 26:
                if count[iIndex + 1] < target:
                    deficit = target - count[iIndex + 1]

                    if count[iIndex] <= target:
                        neededToChange = count[iIndex]
                    else:
                        neededToChange = count[iIndex] - target

                    if deficit > neededToChange:
                        changeOp = neededToChange + (deficit - neededToChange)
                    else:
                        changeOp = deficit + (neededToChange - deficit)

                    calcB = dpArray[iIndex + 2] + count[iIndex] + changeOp + 1
                    dpVal = minVal(dpVal, calcB)

            dpArray[iIndex] = dpVal
            iIndex -= 1

        return dpArray[0]