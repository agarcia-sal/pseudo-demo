from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        def maximum(x: int, y: int) -> int:
            return x if x > y else y

        freqMap = {}
        for element in power:
            freqMap[element] = freqMap.get(element, 0) + 1

        distinctList = list(freqMap.keys())

        def quickSort(arr: List[int], left: int, right: int) -> None:
            if left >= right:
                return
            pivot = arr[(left + right) // 2]
            i, j = left, right
            while i <= j:
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            quickSort(arr, left, j)
            quickSort(arr, i, right)

        quickSort(distinctList, 0, len(distinctList) - 1)

        dpMap = {}

        def recursiveMax(index: int) -> int:
            if index < 0:
                return 0
            if index in dpMap:
                return dpMap[index]

            currentVal = distinctList[index]
            exclVal = recursiveMax(index - 1)

            inclVal = currentVal * freqMap[currentVal]
            searchIndex = index - 1
            while searchIndex >= 0 and distinctList[searchIndex] >= currentVal - 2:
                searchIndex -= 1
            if searchIndex >= 0:
                inclVal += recursiveMax(searchIndex)

            dpMap[index] = maximum(inclVal, exclVal)
            return dpMap[index]

        return recursiveMax(len(distinctList) - 1)