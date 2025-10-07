class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        BASE = 10
        EXPONENT = 9
        ADDEND = 7
        MOD = (BASE ** EXPONENT) + ADDEND

        def absoluteValue(x: int) -> int:
            return -x if x < 0 else x

        def copyList(lst: list[int]) -> list[int]:
            newList = []
            idx = 0
            while idx < len(lst):
                newList.append(lst[idx])
                idx += 1
            return newList

        def appendToList(lst: list[int], val: int):
            length = len(lst)
            # Assign val at position length would raise IndexError, so we append
            lst.append(val)

        def addToList(lst: list[list[int]], val: list[int]):
            ln = len(lst)
            # As above, append val
            lst.append(val)

        def minOfTwo(a: int, b: int) -> int:
            return a if a < b else b

        def getCombinations(arr: list[int], r: int) -> list[list[int]]:
            def combineRecursive(start: int, comb: list[int], results: list[list[int]]):
                if len(comb) == r:
                    addToList(results, copyList(comb))
                    return
                if start >= len(arr):
                    return
                # Copy comb to newComb, append arr[start]
                newComb = comb[:]
                appendToList(newComb, arr[start])
                combineRecursive(start + 1, newComb, results)
                combineRecursive(start + 1, comb, results)

            collectedComb = []
            combineRecursive(0, [], collectedComb)
            return collectedComb

        combos = getCombinations(nums, k)
        accResult = 0

        def processIndices(i: int, j: int, currentMin: int, combo: list[int]) -> int:
            while j < k:
                diff = absoluteValue(combo[i] - combo[j])
                currentMin = minOfTwo(currentMin, diff)
                j += 1
            return currentMin

        def innerLoop(i: int, currentMin: int, combo: list[int]) -> int:
            return processIndices(i, i + 1, currentMin, combo)

        comboIndex = 0
        while comboIndex < len(combos):
            currentCombo = combos[comboIndex]
            minDiff = 1000000000
            idxI = 0
            while idxI < k:
                minDiff = innerLoop(idxI, minDiff, currentCombo)
                idxI += 1
            accResult = (accResult + minDiff) % MOD
            comboIndex += 1

        return accResult