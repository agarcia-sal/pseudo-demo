class Solution:
    def canSortArray(self, nums):
        def bitCount(x):
            def helperCountBits(y, acc):
                if y == 0:
                    return acc
                else:
                    return helperCountBits(y // 2, acc + (y % 2))
            return helperCountBits(x, 0)

        lenNums = 0
        while True:
            if lenNums < len(nums):
                lenNums += 1
            else:
                break

        def copyAndSort(arr):
            def findMinIndex(arrInner, start, bestIndex):
                if start >= len(arrInner):
                    return bestIndex
                else:
                    if arrInner[start] < arrInner[bestIndex]:
                        return findMinIndex(arrInner, start + 1, start)
                    else:
                        return findMinIndex(arrInner, start + 1, bestIndex)

            def selectionSortRec(arrInner, pos):
                if pos == len(arrInner):
                    return arrInner
                else:
                    minIdx = findMinIndex(arrInner, pos, pos)
                    if minIdx != pos:
                        arrInner[pos], arrInner[minIdx] = arrInner[minIdx], arrInner[pos]
                    return selectionSortRec(arrInner, pos + 1)

            newArray = []
            indexCopy = 0
            while indexCopy < len(arr):
                newArray.append(arr[indexCopy])
                indexCopy += 1
            return selectionSortRec(newArray, 0)

        sortedCopy = copyAndSort(nums)

        def outerLoop(m):
            if m >= lenNums:
                return
            else:
                def innerLoop(n):
                    if n >= lenNums - 1:
                        return
                    else:
                        cntA = bitCount(nums[n])
                        cntB = bitCount(nums[n + 1])
                        if cntA == cntB:
                            if nums[n] > nums[n + 1]:
                                nums[n], nums[n + 1] = nums[n + 1], nums[n]
                        innerLoop(n + 1)
                innerLoop(0)
                outerLoop(m + 1)

        outerLoop(0)

        def arraysEqual(a1, a2):
            def compareElements(k):
                if k == len(a1):
                    return True
                else:
                    if a1[k] != a2[k]:
                        return False
                    else:
                        return compareElements(k + 1)
            if len(a1) != len(a2):
                return False
            else:
                return compareElements(0)

        return arraysEqual(nums, sortedCopy)