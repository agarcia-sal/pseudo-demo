from typing import List, Dict

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        def getCount(arr: List[int]) -> Dict[int, int]:
            def accumulateMap(pos: int, mp: Dict[int, int]) -> Dict[int, int]:
                if pos >= len(arr):
                    return mp
                v = arr[pos]
                mp2 = mp.copy()
                if v in mp2:
                    mp2[v] += 1
                else:
                    mp2[v] = 1
                return accumulateMap(pos + 1, mp2)
            return accumulateMap(0, {})

        def sortKeys(mp: Dict[int, int]) -> List[int]:
            ks = list(mp.keys())
            def quicksort(arr: List[int]) -> List[int]:
                if len(arr) <= 1:
                    return arr
                pivot = arr[0]
                smaller = [x for x in arr if x < pivot]
                bigger = [x for x in arr if x > pivot]
                equals = [x for x in arr if x == pivot]
                sortedSmaller = quicksort(smaller)
                sortedBigger = quicksort(bigger)
                return sortedSmaller + equals + sortedBigger
            return quicksort(ks)

        def maxValue(a: int, b: int) -> int:
            return a if a >= b else b

        freqMap = getCount(power)
        sortedArr = sortKeys(freqMap)
        memo: Dict[int, int] = {}

        def processIndex(k: int) -> int:
            if k < 0:
                return 0
            curP = sortedArr[k]
            exclVal = memo.get(sortedArr[k - 1], 0) if k > 0 else 0
            inclVal = curP * freqMap[curP]

            def findJ(j: int) -> int:
                if j < 0:
                    return j
                if sortedArr[j] >= curP - 2:
                    return findJ(j - 1)
                else:
                    return j
            idxJ = findJ(k - 1)
            if idxJ >= 0 and sortedArr[idxJ] in memo:
                inclVal += memo[sortedArr[idxJ]]

            updatedVal = maxValue(inclVal, exclVal)
            memo[curP] = updatedVal
            if k == len(sortedArr) - 1:
                return memo[curP]
            else:
                return processIndex(k + 1)

        if not sortedArr:
            return 0
        _ = processIndex(0)

        res = 0
        for key in memo:
            if memo[key] > res:
                res = memo[key]
        return res