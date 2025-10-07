from collections import defaultdict

class Solution:
    def countPairs(self, waves):
        def customSort(arr):
            def quickSort(a, start, end):
                if start >= end:
                    return
                pivotIndex = start + ((end - start) // 2)
                pivotValue = a[pivotIndex]
                a[pivotIndex], a[end] = a[end], a[pivotIndex]
                storeIndex = start

                def recursivePartition(i):
                    nonlocal storeIndex
                    if i >= end:
                        return
                    if a[i] < pivotValue:
                        a[i], a[storeIndex] = a[storeIndex], a[i]
                        storeIndex += 1
                    recursivePartition(i + 1)

                recursivePartition(start)
                a[storeIndex], a[end] = a[end], a[storeIndex]
                quickSort(a, start, storeIndex - 1)
                quickSort(a, storeIndex + 1, end)

            quickSort(arr, 0, len(arr) - 1)

        customSort(waves)
        totalPairs = 0
        countMap = defaultdict(int)

        def processIndex(current):
            nonlocal totalPairs
            if current >= len(waves):
                return
            visitedElements = {waves[current]}
            stringElements = list(str(waves[current]))
            strLen = len(stringElements)

            def swapElements(arr, idxA, idxB):
                arr[idxA], arr[idxB] = arr[idxB], arr[idxA]

            def innerLoop1(j):
                if j > strLen - 1:
                    return

                def innerLoop2(i):
                    if i >= j:
                        return
                    swapElements(stringElements, i, j)
                    combinedNum = int("".join(stringElements))
                    visitedElements.add(combinedNum)

                    def innerLoop3(q):
                        if q > strLen - 1:
                            return

                        def innerLoop4(p):
                            if p >= q:
                                return
                            swapElements(stringElements, p, q)
                            tempNum = int("".join(stringElements))
                            visitedElements.add(tempNum)
                            swapElements(stringElements, p, q)
                            innerLoop4(p + 1)

                        innerLoop4(q - 1)
                        innerLoop3(q + 1)

                    innerLoop3(i + 1)
                    swapElements(stringElements, i, j)
                    innerLoop2(i + 1)

                innerLoop2(0)
                innerLoop1(j + 1)

            innerLoop1(0)

            sumCounts = 0
            for element in visitedElements:
                if element in countMap:
                    sumCounts += countMap[element]

            totalPairs += sumCounts
            countMap[waves[current]] += 1
            processIndex(current + 1)

        processIndex(0)
        return totalPairs