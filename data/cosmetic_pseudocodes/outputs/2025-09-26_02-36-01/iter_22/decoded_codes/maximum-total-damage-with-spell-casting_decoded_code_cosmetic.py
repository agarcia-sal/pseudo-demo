from typing import List, Dict, Optional

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        def replicateCountMapping(array: List[int]) -> Dict[int, int]:
            auxCount = {}
            idxA = 0
            while idxA < len(array):
                currentVal = array[idxA]
                if currentVal not in auxCount:
                    auxCount[currentVal] = 0
                auxCount[currentVal] += 1
                idxA += 1
            return auxCount

        countMap = replicateCountMapping(power)

        uniqueValues = list(countMap.keys())
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(uniqueValues) - 1):
                if uniqueValues[i] > uniqueValues[i + 1]:
                    uniqueValues[i], uniqueValues[i + 1] = uniqueValues[i + 1], uniqueValues[i]
                    swapped = True

        dpMap: Dict[int, int] = {}
        pos = 0
        while pos < len(uniqueValues):
            powerEntry = uniqueValues[pos]
            exclVal = dpMap.get(uniqueValues[pos - 1], 0) if pos > 0 else 0

            includeVal = powerEntry * countMap[powerEntry]
            wIdx = pos - 1
            while wIdx >= 0 and uniqueValues[wIdx] >= powerEntry - 2:
                wIdx -= 1
            if wIdx >= 0:
                includeVal += dpMap.get(uniqueValues[wIdx], 0)

            dpMap[powerEntry] = includeVal if includeVal > exclVal else exclVal
            pos += 1

        maxVal: Optional[int] = None
        for k in dpMap:
            if maxVal is None or dpMap[k] > maxVal:
                maxVal = dpMap[k]

        return maxVal if maxVal is not None else 0