from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        frequencyMap = {}
        for element in power:
            frequencyMap[element] = frequencyMap.get(element, 0) + 1

        sortedKeys = sorted(frequencyMap.keys())
        dpCache = {}
        position = 0
        n = len(sortedKeys)

        while position < n:
            currentValue = sortedKeys[position]

            if position == 0:
                optExclude = 0
            else:
                prevKey = sortedKeys[position - 1]
                optExclude = dpCache.get(prevKey, 0)

            damageValue = currentValue * frequencyMap[currentValue]

            backIndex = position - 1
            while backIndex >= 0 and sortedKeys[backIndex] >= currentValue - 2:
                backIndex -= 1

            if backIndex >= 0:
                damageValue += dpCache[sortedKeys[backIndex]]

            dpCache[currentValue] = damageValue if damageValue > optExclude else optExclude
            position += 1

        return max(dpCache.values()) if dpCache else 0