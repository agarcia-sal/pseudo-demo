from typing import List, Dict

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        def getMax(arr: List[int]) -> int:
            idx = 1
            lim = len(arr)
            currentMax = arr[0]
            while idx < lim:
                if arr[idx] > currentMax:
                    currentMax = arr[idx]
                idx += 1
            return currentMax

        def countElements(arr: List[int]) -> Dict[int, int]:
            dictCount = {}
            p = 0
            n = len(arr)
            while p < n:
                elem = arr[p]
                if elem in dictCount:
                    dictCount[elem] += 1
                else:
                    dictCount[elem] = 1
                p += 1
            return dictCount

        def cumulativeSum(lst: List[int]) -> List[int]:
            acc = []
            cumVal = 0
            sidx = 0
            while sidx < len(lst):
                cumVal += lst[sidx]
                acc.append(cumVal)
                sidx += 1
            return acc

        def bisectRight(arr: List[int], val: int) -> int:
            low = 0
            high = len(arr)
            while low < high:
                median = low + (high - low) // 2
                if val < arr[median]:
                    high = median
                else:
                    low = median + 1
            return low

        maximumValue = getMax(nums)
        frequencyMap = countElements(nums)
        gcdCounters = [0] * (maximumValue + 1)

        def computeAtI(indexI: int):
            if indexI < 1:
                return
            accumulatorVar = 0
            def innerLoop(idxJ: int):
                nonlocal accumulatorVar
                if idxJ > maximumValue:
                    return
                freqJ = frequencyMap.get(idxJ, 0)
                accumulatorVar += freqJ
                gcdCounters[indexI] -= gcdCounters[idxJ]
                innerLoop(idxJ + indexI)
            innerLoop(indexI)
            gcdCounters[indexI] += (accumulatorVar * (accumulatorVar - 1)) // 2
            computeAtI(indexI - 1)

        computeAtI(maximumValue)

        prefixSums = cumulativeSum(gcdCounters)
        answers = []

        def processQueries(pos: int):
            if pos >= len(queries):
                return
            queryVal = queries[pos]
            insertPos = bisectRight(prefixSums, queryVal)
            answers.append(insertPos)
            processQueries(pos + 1)

        processQueries(0)
        return answers