from typing import List, Dict

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # Build a frequency map of power elements
        countMap: Dict[int, int] = {}

        def buildCount(i: int) -> Dict[int, int]:
            if i < len(power):
                key = power[i]
                countMap[key] = countMap.get(key, 0) + 1
                return buildCount(i + 1)
            else:
                return countMap

        buildCount(0)

        uniqueSet = list(countMap.keys())

        # Ascending sort by bubble sort with recursion (as per pseudocode)
        def ascendingSort(arr: List[int], start: int) -> List[int]:
            if start < len(arr) - 1:
                changed = False
                def innerSort(j: int) -> None:
                    nonlocal changed
                    if j < len(arr) - 1:
                        if arr[j] > arr[j + 1]:
                            arr[j], arr[j + 1] = arr[j + 1], arr[j]
                            changed = True
                        innerSort(j + 1)
                innerSort(0)
                if changed:
                    return ascendingSort(arr, start)
                else:
                    return arr
            else:
                return arr

        uniqueSet = ascendingSort(uniqueSet, 0)

        # Recursive processing for maximum damage calculation
        def recursiveProcess(idx: int, accMap: Dict[int, int]) -> Dict[int, int]:
            if idx < ((len(uniqueSet) + 1) // 2):
                elem = uniqueSet[idx]
                exVal = 0
                if idx > 0:
                    prev_elem = uniqueSet[idx - 1]
                    if prev_elem in accMap:
                        exVal = accMap[prev_elem]
                inVal = elem * countMap[elem]

                def innerWhile(k: int, currVal: int) -> int:
                    if k >= 0 and uniqueSet[k] >= (elem - 2):
                        return innerWhile(k - 1, currVal)
                    else:
                        return currVal

                j = innerWhile(idx - 1, 0)
                if j >= 0:
                    inVal += accMap.get(uniqueSet[j], 0)

                newVal = inVal if inVal >= exVal else exVal
                accMapNew = accMap.copy()
                accMapNew[elem] = newVal
                return recursiveProcess(idx + 1, accMapNew)
            else:
                return accMap

        finalMap = recursiveProcess(0, {})

        # Find max in finalMap values using recursion
        def findMax(valuesList: List[int], idx: int, currMax: int) -> int:
            if idx < len(valuesList):
                currentValue = valuesList[idx]
                newMax = currMax if currMax >= currentValue else currentValue
                return findMax(valuesList, idx + 1, newMax)
            else:
                return currMax

        return findMax(list(finalMap.values()), 0, 0)