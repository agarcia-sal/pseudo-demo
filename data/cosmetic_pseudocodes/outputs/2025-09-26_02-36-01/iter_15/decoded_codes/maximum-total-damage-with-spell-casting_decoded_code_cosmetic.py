from typing import List, Dict

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freqMap: Dict[int, int] = {}
        uniqueList: List[int] = []
        resultMap: Dict[int, int] = {}

        def tally(elements: List[int]) -> None:
            for val in elements:
                freqMap[val] = freqMap.get(val, 0) + 1

        tally(power)

        uniqueList = list(freqMap.keys())

        def quickSort(arr: List[int], left: int, right: int) -> None:
            if left >= right:
                return
            pivotIndex = left
            i = left + 1
            j = right
            while True:
                while i <= right and arr[i] < arr[pivotIndex]:
                    i += 1
                while j > left and arr[j] > arr[pivotIndex]:
                    j -= 1
                if i > j:
                    break
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            arr[pivotIndex], arr[j] = arr[j], arr[pivotIndex]
            quickSort(arr, left, j - 1)
            quickSort(arr, j + 1, right)

        quickSort(uniqueList, 0, len(uniqueList) - 1)

        def getVal(mapping: Dict[int, int], key: int) -> int:
            return mapping.get(key, 0)

        idx = 0
        n = len(uniqueList)
        while idx < n:
            currentKey = uniqueList[idx]
            valExcl = getVal(resultMap, uniqueList[idx - 1]) if idx > 0 else 0
            valIncl = currentKey * freqMap[currentKey]
            backIdx = idx - 1
            while backIdx >= 0 and uniqueList[backIdx] >= currentKey - 2:
                backIdx -= 1
            if backIdx >= 0:
                valIncl += getVal(resultMap, uniqueList[backIdx])
            resultMap[currentKey] = valIncl if valIncl > valExcl else valExcl
            idx += 1

        maxVal = 0
        for v in resultMap.values():
            if v > maxVal:
                maxVal = v
        return maxVal